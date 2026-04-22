from __future__ import annotations

import argparse
import hashlib
import html
import os
import re
import shutil
from collections import defaultdict
from pathlib import Path
from typing import Iterable
from urllib.parse import quote, unquote, urlsplit, urlunsplit


IMAGE_EXTENSIONS = {".png", ".jpg", ".jpeg", ".svg", ".gif", ".webp", ".bmp", ".ico"}
EXCLUDED_PARTS = {".git", ".codex-tmp", "__pycache__", "outputs", "_resolved", "_unmigrated"}
HTML_IMAGE_REF_RE = re.compile(
    r'(?P<prefix>\b(?:src|href)=["\'])(?P<url>[^"\']+\.(?:png|svg|jpe?g|gif|webp|bmp|ico)(?:[?#][^"\']*)?)(?P<suffix>["\'])',
    re.IGNORECASE,
)
MARKDOWN_IMAGE_REF_RE = re.compile(
    r'(?P<prefix>!?\[[^\]]*\]\(\s*<?)(?P<url>[^)>]+?\.(?:png|svg|jpe?g|gif|webp|bmp|ico)(?:[?#][^)>]*)?)(?P<suffix>>?\s*\))',
    re.IGNORECASE,
)


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def sanitize_name(text: str) -> str:
    result = re.sub(r"[^a-z0-9._-]+", "-", text.lower()).strip("-")
    return result or "asset"


def iter_asset_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in IMAGE_EXTENSIONS:
            continue
        if "assets" not in path.parts:
            continue
        if set(path.parts) & EXCLUDED_PARTS:
            continue
        yield path


def build_duplicate_groups(root: Path) -> list[list[Path]]:
    groups: dict[str, list[Path]] = defaultdict(list)
    for path in iter_asset_files(root):
        groups[sha256_file(path)].append(path)
    return [sorted(paths) for paths in groups.values() if len(paths) > 1]


def canonical_shared_path(root: Path, hash_value: str, source: Path) -> Path:
    shared_dir = root / "_assets" / "shared-images" / hash_value[:2]
    file_name = f"{hash_value[:12]}-{sanitize_name(source.stem)}{source.suffix.lower()}"
    return shared_dir / file_name


def build_rewrite_map(root: Path) -> tuple[dict[Path, Path], dict[Path, str]]:
    rewrite_map: dict[Path, Path] = {}
    hash_by_path: dict[Path, str] = {}
    for group in build_duplicate_groups(root):
        hash_value = sha256_file(group[0])
        shared_path = canonical_shared_path(root, hash_value, group[0])
        shared_path.parent.mkdir(parents=True, exist_ok=True)
        if not shared_path.exists():
            shutil.copy2(group[0], shared_path)
        for asset_path in group:
            rewrite_map[asset_path.resolve()] = shared_path.resolve()
            hash_by_path[asset_path.resolve()] = hash_value
    return rewrite_map, hash_by_path


def is_local_url(url: str) -> bool:
    lowered = (url or "").strip().lower()
    if not lowered:
        return False
    if lowered.startswith(("#", "data:", "blob:", "mailto:", "tel:")):
        return False
    if re.match(r"^(?:[a-z]+:)?//", lowered):
        return False
    return True


def resolve_markdown_url(root: Path, markdown_path: Path, raw_url: str) -> Path | None:
    if not is_local_url(raw_url):
        return None
    decoded = html.unescape(raw_url.strip())
    if decoded.startswith("<") and decoded.endswith(">"):
        decoded = decoded[1:-1].strip()
    parts = urlsplit(decoded)
    if parts.scheme or parts.netloc:
        return None
    path_part = unquote(parts.path)
    if not path_part:
        return None
    if path_part.startswith("/"):
        return (root / path_part.lstrip("/")).resolve()
    return (markdown_path.parent / path_part).resolve()


def to_site_absolute_url(root: Path, target_path: Path, original_url: str) -> str:
    decoded = html.unescape(original_url.strip())
    had_brackets = decoded.startswith("<") and decoded.endswith(">")
    if had_brackets:
        decoded = decoded[1:-1].strip()
    parts = urlsplit(decoded)
    relative_path = target_path.resolve().relative_to(root.resolve()).as_posix()
    new_url = "/" + quote(relative_path, safe="/._-")
    if parts.query or parts.fragment:
        new_url = urlunsplit(("", "", new_url, parts.query, parts.fragment))
    if had_brackets or " " in new_url:
        return f"<{new_url}>"
    return new_url


def rewrite_markdown_file(root: Path, markdown_path: Path, rewrite_map: dict[Path, Path]) -> bool:
    original = markdown_path.read_text(encoding="utf-8", errors="ignore")
    updated = original

    def replace_match(match: re.Match[str]) -> str:
        url = match.group("url")
        resolved = resolve_markdown_url(root, markdown_path, url)
        if not resolved:
            return match.group(0)
        replacement_path = rewrite_map.get(resolved)
        if not replacement_path:
            return match.group(0)
        new_url = to_site_absolute_url(root, replacement_path, url)
        return f"{match.group('prefix')}{new_url}{match.group('suffix')}"

    updated = HTML_IMAGE_REF_RE.sub(replace_match, updated)
    updated = MARKDOWN_IMAGE_REF_RE.sub(replace_match, updated)

    if updated != original:
        markdown_path.write_text(updated, encoding="utf-8")
        return True
    return False


def iter_markdown_files(root: Path) -> Iterable[Path]:
    for path in root.rglob("*.md"):
        if set(path.parts) & EXCLUDED_PARTS:
            continue
        yield path


def rewrite_markdown_references(root: Path, rewrite_map: dict[Path, Path]) -> int:
    changed_files = 0
    for markdown_path in iter_markdown_files(root):
        if rewrite_markdown_file(root, markdown_path, rewrite_map):
            changed_files += 1
    return changed_files


def verify_local_image_references(root: Path) -> list[tuple[Path, str]]:
    missing: list[tuple[Path, str]] = []
    for markdown_path in iter_markdown_files(root):
        text = markdown_path.read_text(encoding="utf-8", errors="ignore")
        for pattern in (HTML_IMAGE_REF_RE, MARKDOWN_IMAGE_REF_RE):
            for match in pattern.finditer(text):
                url = match.group("url")
                resolved = resolve_markdown_url(root, markdown_path, url)
                if resolved and not resolved.exists():
                    missing.append((markdown_path, url))
    return missing


def delete_duplicate_assets(rewrite_map: dict[Path, Path]) -> int:
    deleted = 0
    for source_path, target_path in rewrite_map.items():
        if source_path == target_path:
            continue
        if source_path.exists():
            source_path.unlink()
            deleted += 1
    return deleted


def main() -> int:
    parser = argparse.ArgumentParser(description="Deduplicate exact image copies stored in page assets folders.")
    parser.add_argument("--root", default=".", help="Repository root")
    parser.add_argument("--dry-run", action="store_true", help="Do not modify files")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    rewrite_map, hash_by_path = build_rewrite_map(root)
    duplicate_groups = len(set(hash_by_path.values()))
    duplicate_files = len(rewrite_map)

    print(f"Duplicate groups: {duplicate_groups}")
    print(f"Duplicate files involved: {duplicate_files}")

    if args.dry_run:
        return 0

    changed_markdown_files = rewrite_markdown_references(root, rewrite_map)
    deleted_assets = delete_duplicate_assets(rewrite_map)
    missing_refs = verify_local_image_references(root)
    if missing_refs:
        for markdown_path, url in missing_refs[:50]:
            print(f"MISSING {markdown_path}: {url}")
        raise SystemExit(f"Verification failed: {len(missing_refs)} broken local image references remain.")

    print(f"Changed markdown files: {changed_markdown_files}")
    print(f"Deleted duplicate assets: {deleted_assets}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
