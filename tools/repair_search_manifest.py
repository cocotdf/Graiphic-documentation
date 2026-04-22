from __future__ import annotations

import argparse
import html
import json
from pathlib import Path


CP1252_UNICODE_TO_BYTE = {
    0x20AC: 0x80,
    0x201A: 0x82,
    0x0192: 0x83,
    0x201E: 0x84,
    0x2026: 0x85,
    0x2020: 0x86,
    0x2021: 0x87,
    0x02C6: 0x88,
    0x2030: 0x89,
    0x0160: 0x8A,
    0x2039: 0x8B,
    0x0152: 0x8C,
    0x017D: 0x8E,
    0x2018: 0x91,
    0x2019: 0x92,
    0x201C: 0x93,
    0x201D: 0x94,
    0x2022: 0x95,
    0x2013: 0x96,
    0x2014: 0x97,
    0x02DC: 0x98,
    0x2122: 0x99,
    0x0161: 0x9A,
    0x203A: 0x9B,
    0x0153: 0x9C,
    0x017E: 0x9E,
    0x0178: 0x9F,
}

SUSPECT_CODEPOINTS = {
    0x009D,
    0x00C2,
    0x00C3,
    0x00E2,
    0x0153,
    0x201A,
    0x201C,
    0x201D,
    0x2020,
    0x2021,
    0x2039,
    0x20AC,
    0x2122,
}


def has_mojibake(text: str) -> bool:
    return any(ord(ch) in SUSPECT_CODEPOINTS for ch in text)


def encode_mixed_cp1252(text: str) -> bytes:
    data = bytearray()
    for ch in text:
        code = ord(ch)
        if code <= 0xFF:
            data.append(code)
            continue
        if code in CP1252_UNICODE_TO_BYTE:
            data.append(CP1252_UNICODE_TO_BYTE[code])
            continue
        raise ValueError(f"Unsupported codepoint {code} in candidate mojibake text")
    return bytes(data)


def repair_text(text: str) -> str:
    current = html.unescape(text or "")
    for _ in range(3):
        if not has_mojibake(current):
            break
        try:
            repaired = encode_mixed_cp1252(current).decode("utf-8")
        except (UnicodeDecodeError, ValueError):
            break
        if repaired == current:
            break
        current = repaired
    current = current.replace("\u009d", " ")
    return " ".join(current.split())


def repair_manifest(path: Path) -> tuple[int, int]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    changed_fields = 0
    changed_items = 0
    for item in payload.get("items", []):
        item_changed = False
        for key in ("title", "keywords", "content"):
            value = item.get(key)
            if not isinstance(value, str):
                continue
            repaired = repair_text(value)
            if repaired != value:
                item[key] = repaired
                changed_fields += 1
                item_changed = True
        if item_changed:
            changed_items += 1
    path.write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return changed_fields, changed_items


def main() -> int:
    parser = argparse.ArgumentParser(description="Repair mojibake and dirty text inside search-manifest.json.")
    parser.add_argument("manifest", nargs="?", default="search-manifest.json", help="Path to the search manifest JSON file.")
    args = parser.parse_args()

    manifest_path = Path(args.manifest).resolve()
    changed_fields, changed_items = repair_manifest(manifest_path)
    print(f"Repaired {changed_fields} fields across {changed_items} entries in {manifest_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
