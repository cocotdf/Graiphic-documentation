import csv
import html
import json
import math
import re
import unicodedata
from collections import Counter
from collections import defaultdict
from difflib import SequenceMatcher
from pathlib import Path


BASE_URL = "https://graiphic.github.io/Graiphic-documentation/#"
ROOT_MAP = {
    "ComputerVision": ("computer-vision",),
    "DeepLearning": ("deep-learning",),
    "Accelerator": ("accelerator",),
    "GenAI": ("genai",),
}
TOKEN_EQUIV = {
    "idx": "index",
    "indices": "index",
    "bool": "boolean",
    "samplers": "sampler",
    "imgs": "image",
    "img": "image",
    "rois": "roi",
    "weights": "weight",
    "params": "parameter",
    "coeff": "coefficient",
    "norm": "normalization",
    "exec": "execution",
    "fw": "forward",
    "bw": "backward",
    "init": "initialize",
    "sgl": "single",
    "dbl": "double",
    "u8": "uint8",
    "u16": "uint16",
    "u32": "uint32",
    "u64": "uint64",
    "i8": "int8",
    "i16": "int16",
    "i32": "int32",
    "i64": "int64",
    "acc": "",
    "miniaudio": "audio",
}
STOP = {
    "readme",
    "vi",
    "methods",
    "method",
    "source",
    "subvis",
    "functions",
    "function",
    "tool",
    "tools",
    "advanced",
    "quick",
    "start",
    "embedded",
    "simplified",
    "onnx",
    "array",
    "cluster",
    "labview",
    "dl",
    "poly",
}
SOURCE_PART_ALIASES = {
    "miniaudio": "Audio Process",
}
SOURCE_SKIP_PARTS = {
    "source",
    "methods",
    "method",
    "_methods",
    "_method",
    "subvis",
}
MARKER_WEIGHTS = {
    "output": 2.6,
    "input": 1.8,
    "loss": 2.4,
    "forward": 1.6,
    "backward": 1.7,
    "train": 1.3,
    "inference": 1.5,
    "academic": 1.0,
    "mono": 0.8,
    "multi": 0.8,
    "name": 0.7,
    "index": 0.7,
    "scalar": 0.9,
    "1d": 0.9,
    "2d": 0.9,
    "3d": 0.9,
    "4d": 0.9,
    "5d": 0.9,
    "6d": 0.9,
    "add_to_graph": 2.4,
    "graph": 1.2,
    "open": 1.0,
    "close": 1.0,
    "set": 0.8,
    "get": 0.8,
    "create": 0.9,
}
THRESHOLD = 0.46

CAMEL_1 = re.compile(r"([a-z])([A-Z])")
CAMEL_2 = re.compile(r"([A-Za-z])([0-9])")
CAMEL_3 = re.compile(r"([0-9])([A-Za-z])")
WORD_RE = re.compile(r"[a-z0-9]+")
HTML_DESCRIPTION_RE = re.compile(
    r"<h2>\s*Description\s*</h2>(.*?)(?:<h3>\s*Input parameters\s*</h3>|<h2>\s*Example[s]?\s*</h2>|$)",
    re.IGNORECASE | re.DOTALL,
)
MARKDOWN_DESCRIPTION_RE = re.compile(
    r"^\s*##\s*Description\s*$([\s\S]*?)(?=^\s*###\s*Input parameters\s*$|^\s*##\s*Example[s]?\s*$|\Z)",
    re.IGNORECASE | re.MULTILINE,
)


def ascii_lower(text: str) -> str:
    text = unicodedata.normalize("NFKD", text)
    text = text.encode("ascii", "ignore").decode("ascii")
    return text.lower()


def expand_text(text: str) -> str:
    text = text.replace("&", " and ")
    for char in "><()[]{}":
        text = text.replace(char, " ")
    text = text.replace("/", " ").replace("\\", " ").replace("_", " ").replace("-", " ")
    text = CAMEL_1.sub(r"\1 \2", text)
    text = CAMEL_2.sub(r"\1 \2", text)
    text = CAMEL_3.sub(r"\1 \2", text)
    return ascii_lower(text)


def tokenize(text: str) -> list[str]:
    tokens: list[str] = []
    for token in WORD_RE.findall(expand_text(text)):
        token = TOKEN_EQUIV.get(token, token)
        if not token:
            continue
        if token.endswith("s") and len(token) > 4 and token not in {"loss", "bias"}:
            token = token[:-1]
        if token and token not in STOP:
            tokens.append(token)
    return tokens


def norm_phrase(text: str) -> str:
    return " ".join(tokenize(text))


def split_source_parts(source_path: str) -> list[str]:
    return [part for part in re.split(r"[\\/]+", source_path) if part]


def source_root_key(source_parts: list[str]) -> str:
    for part in source_parts:
        for root in ROOT_MAP:
            if part.lower() == root.lower():
                return root
    compact_source = re.sub(r"[^a-z0-9]+", "", ascii_lower(" ".join(source_parts)))
    for root in ROOT_MAP:
        compact_root = re.sub(r"[^a-z0-9]+", "", ascii_lower(root))
        if compact_root and compact_root in compact_source:
            return root
    return source_parts[0] if source_parts else ""


def source_parts_for_matching(source_path: str) -> list[str]:
    raw_parts = split_source_parts(source_path)
    root = source_root_key(raw_parts)
    compact_root = re.sub(r"[^a-z0-9]+", "", ascii_lower(root))
    trimmed = False
    for index, part in enumerate(raw_parts):
        if part.lower() == root.lower():
            raw_parts = raw_parts[index + 1 :]
            trimmed = True
            break
    if not trimmed and compact_root:
        for index, part in enumerate(raw_parts):
            compact_part = re.sub(r"[^a-z0-9]+", "", ascii_lower(part))
            if compact_root in compact_part:
                raw_parts = raw_parts[index + 1 :]
                break

    parts: list[str] = []
    for raw_part in raw_parts:
        stem = Path(raw_part).stem if raw_part.lower().endswith(".vi") else raw_part
        lowered = ascii_lower(stem).strip()
        lowered_key = lowered.strip("_")
        if lowered in SOURCE_SKIP_PARTS or lowered_key in SOURCE_SKIP_PARTS:
            continue
        parts.append(SOURCE_PART_ALIASES.get(lowered, stem))

    return parts


def source_match_text(source_path: str) -> str:
    return " ".join(source_parts_for_matching(source_path))


def effective_menu_text(source_path: str, menu_name: str) -> str:
    return menu_name if menu_name.strip() else source_match_text(source_path)


def effective_menu_segments(source_path: str, menu_name: str) -> list[str]:
    if menu_name.strip():
        return [segment.strip() for segment in menu_name.split(":") if segment.strip()]
    return source_parts_for_matching(source_path)


def lcs_len(left: list[str], right: list[str]) -> int:
    rows = len(left)
    cols = len(right)
    table = [0] * (cols + 1)
    for row_idx in range(1, rows + 1):
        previous = 0
        for col_idx in range(1, cols + 1):
            current = table[col_idx]
            if left[row_idx - 1] == right[col_idx - 1]:
                table[col_idx] = previous + 1
            else:
                table[col_idx] = max(table[col_idx], table[col_idx - 1])
            previous = current
    return table[cols]


def extract_markers(source_path: str, menu_name: str) -> set[str]:
    source_lower = ascii_lower(source_path)
    menu_text = effective_menu_text(source_path, menu_name)
    menu_lower = ascii_lower(menu_text)
    tokens = set(tokenize(source_path + " " + menu_text + " " + source_match_text(source_path)))
    markers = {token for token in tokens if token in MARKER_WEIGHTS}

    if "mono_output" in source_lower or "multi_output" in source_lower or "output" in source_lower:
        markers.add("output")
    if "input" in source_lower or menu_lower.startswith("input:"):
        markers.add("input")
    if "loss input" in menu_lower or "y_true" in source_lower:
        markers.update({"loss", "input"})
    if "train backward" in menu_lower:
        markers.update({"train", "backward"})
    if "train forward" in menu_lower:
        markers.update({"train", "forward"})
    if "inference" in menu_lower or "infer" in source_lower:
        markers.add("inference")
    if "academic" in source_lower or "academic" in menu_lower:
        markers.add("academic")
    if "add_to_graph" in source_lower:
        markers.update({"add_to_graph", "graph"})
    if "\\open" in source_lower or menu_lower.startswith("open"):
        markers.add("open")
    if menu_lower.startswith("close"):
        markers.add("close")
    if menu_lower.startswith("set:") or ":set:" in menu_lower:
        markers.add("set")
    if menu_lower.startswith("get:") or ":get:" in menu_lower:
        markers.add("get")
    if menu_lower.startswith("create") or "create" in source_lower:
        markers.add("create")

    return markers


def weighted_overlap(query_tokens: list[str], candidate_tokens: list[str], idf: dict[str, float]) -> float:
    if not query_tokens:
        return 0.0

    candidate_set = set(candidate_tokens)
    query_counter = Counter(query_tokens)
    numerator = 0.0
    denominator = 0.0

    for token, count in query_counter.items():
        weight = idf.get(token, 1.0) * count
        denominator += weight
        if token in candidate_set:
            numerator += weight

    return numerator / denominator if denominator else 0.0


def segment_score(menu_segments: list[str], candidate: dict, idf: dict[str, float]) -> float:
    if not menu_segments:
        return 0.0

    phrases = candidate["seg_phrases"] + [candidate["title_phrase"], candidate["full_phrase"]]
    values: list[float] = []
    for segment in menu_segments:
        segment_phrase = norm_phrase(segment)
        if not segment_phrase:
            continue

        best = 0.0
        for phrase in phrases:
            if not phrase:
                continue
            ratio = SequenceMatcher(None, segment_phrase, phrase).ratio()
            token_bonus = weighted_overlap(tokenize(segment), tokenize(phrase), idf)
            best = max(best, 0.45 * ratio + 0.55 * token_bonus)
        values.append(best)

    return sum(values) / len(values) if values else 0.0


def seq_token_score(query_tokens: list[str], candidate_tokens: list[str]) -> float:
    if not query_tokens or not candidate_tokens:
        return 0.0
    return lcs_len(query_tokens, candidate_tokens) / max(1, len(query_tokens))


def candidate_markers(candidate: dict) -> set[str]:
    markers = set()
    for token in set(candidate["all_tokens"]):
        if token in MARKER_WEIGHTS:
            markers.add(token)

    for token in (
        "input",
        "output",
        "loss",
        "forward",
        "backward",
        "train",
        "inference",
        "academic",
        "mono",
        "multi",
        "name",
        "index",
        "scalar",
        "1d",
        "2d",
        "3d",
        "4d",
        "5d",
        "6d",
        "graph",
        "open",
        "close",
        "set",
        "get",
        "create",
        "execution",
    ):
        if token in candidate["full_phrase"]:
            markers.add(token)

    return markers


def marker_alignment(source_markers: set[str], candidate_markers_set: set[str]) -> float:
    if not source_markers:
        return 0.0

    denominator = sum(MARKER_WEIGHTS[marker] for marker in source_markers)
    numerator = sum(MARKER_WEIGHTS[marker] for marker in source_markers if marker in candidate_markers_set)
    return numerator / denominator if denominator else 0.0


def structural_bonus(source_path: str, candidate: dict) -> float:
    source_lower = ascii_lower(source_path)
    candidate_path = candidate["path"].lower()
    candidate_markers_set = candidate["markers"]
    bonus = 0.0

    if "mono_output" in source_lower or "multi_output" in source_lower:
        if "output" in candidate_markers_set:
            bonus += 0.08
        if "exec" in candidate_markers_set or "execution" in candidate_markers_set:
            bonus -= 0.03
    if "add_to_cluster_onnx_y_true" in source_lower and "loss" in candidate_markers_set:
        bonus += 0.07
    if "add_to_cluster_onnx_input" in source_lower and (
        "input" in candidate_markers_set or {"name", "index"} & candidate_markers_set
    ):
        bonus += 0.03
    if "add_to_graph" in source_lower and "graph" in candidate_markers_set:
        bonus += 0.05
    if "miniaudio" in source_lower:
        if candidate_path.startswith("/genai/audio-process/"):
            bonus += 0.18
        elif candidate["root"] == "genai":
            bonus -= 0.08

    return bonus


def mismatch_penalty(source_markers: set[str], candidate_markers_set: set[str]) -> float:
    penalty = 0.0

    if "output" in source_markers and "input" in candidate_markers_set and "output" not in candidate_markers_set:
        penalty += 0.16
    if "output" in source_markers and (
        "exec" in candidate_markers_set or "execution" in candidate_markers_set
    ) and "output" not in candidate_markers_set:
        penalty += 0.09
    if "input" in source_markers and "output" in candidate_markers_set and "input" not in candidate_markers_set:
        penalty += 0.08
    if "loss" in source_markers and "forward" in candidate_markers_set:
        penalty += 0.08
    if "loss" in source_markers and "loss" not in candidate_markers_set:
        penalty += 0.08
    if "backward" in source_markers and "forward" in candidate_markers_set:
        penalty += 0.05
    if "forward" in source_markers and "backward" in candidate_markers_set:
        penalty += 0.04
    if "add_to_graph" in source_markers and not ({"graph", "add_to_graph"} & candidate_markers_set):
        penalty += 0.18
    if "add_to_graph" in source_markers and {"input", "output", "exec", "execution"} & candidate_markers_set:
        penalty += 0.12

    return penalty


def clean_description_text(text: str) -> str:
    original_text = text
    text = html.unescape(text)
    try:
        repaired = text.encode("latin-1", errors="ignore").decode("utf-8", errors="ignore")
        original_noise = sum(original_text.count(char) + text.count(char) for char in ("â", "Â", "Ã"))
        repaired_noise = sum(repaired.count(char) for char in ("â", "Â", "Ã"))
        if repaired and repaired_noise < original_noise:
            text = repaired
    except UnicodeError:
        pass
    text = text.replace("\ufeff", " ")
    text = text.replace("\u00a0", " ")
    text = text.replace("Â", " ")
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_description_text(doc_path: Path) -> str:
    if not doc_path.exists():
        return ""

    text = doc_path.read_text(encoding="utf-8", errors="ignore")

    html_match = HTML_DESCRIPTION_RE.search(text)
    if html_match:
        section = html_match.group(1)
        section = re.split(r"<p[^>]*>\s*<img\b", section, maxsplit=1, flags=re.IGNORECASE)[0]
        section = re.split(r"<img\b", section, maxsplit=1, flags=re.IGNORECASE)[0]
        return clean_description_text(section)

    markdown_match = MARKDOWN_DESCRIPTION_RE.search(text)
    if markdown_match:
        section = markdown_match.group(1)
        section = re.split(r"^\s*!\[", section, maxsplit=1, flags=re.MULTILINE)[0]
        return clean_description_text(section)

    return ""


def build_candidates(manifest_path: Path) -> tuple[list[dict], dict[str, float]]:
    items = json.loads(manifest_path.read_text(encoding="utf-8"))["items"]
    document_frequency: Counter[str] = Counter()
    candidates: list[dict] = []

    for item in items:
        path = item["path"]
        parts = [part for part in path.split("/") if part]
        root = parts[0] if parts else ""
        segments = [segment for segment in parts[1:] if segment.lower() != "readme.md"]
        title_tokens = tokenize(item.get("title", ""))
        path_tokens = tokenize("/".join(segments))
        keyword_tokens = tokenize(item.get("keywords", ""))
        all_tokens = set(title_tokens + path_tokens + keyword_tokens)

        for token in all_tokens:
            document_frequency[token] += 1

        candidates.append(
            {
                "title": item.get("title", ""),
                "path": path,
                "root": root,
                "segments": segments,
                "seg_phrases": [norm_phrase(segment.replace(".md", "")) for segment in segments],
                "title_phrase": norm_phrase(item.get("title", "")),
                "path_tokens": path_tokens,
                "title_tokens": title_tokens,
                "keyword_tokens": keyword_tokens,
                "all_tokens": list(all_tokens),
                "token_set": set(all_tokens),
                "leaf_phrase": norm_phrase(segments[-1]) if segments else norm_phrase(item.get("title", "")),
                "full_phrase": norm_phrase(
                    item.get("keywords", "") + " " + "/".join(segments) + " " + item.get("title", "")
                ),
            }
        )

    total = len(items)
    idf = {token: math.log((total + 1) / (count + 1)) + 1.0 for token, count in document_frequency.items()}
    for candidate in candidates:
        candidate["markers"] = candidate_markers(candidate)

    return candidates, idf


def build_indexes(candidates: list[dict]) -> dict[str, dict]:
    root_indexes: dict[str, list[int]] = defaultdict(list)
    token_indexes: dict[str, dict[str, set[int]]] = defaultdict(lambda: defaultdict(set))
    marker_indexes: dict[str, dict[str, set[int]]] = defaultdict(lambda: defaultdict(set))

    for idx, candidate in enumerate(candidates):
        root = candidate["root"]
        root_indexes[root].append(idx)
        for token in set(candidate["all_tokens"]):
            token_indexes[root][token].add(idx)
        for marker in candidate["markers"]:
            marker_indexes[root][marker].add(idx)

    return {
        "roots": root_indexes,
        "tokens": token_indexes,
        "markers": marker_indexes,
    }


def score_candidate(source_path: str, menu_name: str, candidate: dict, idf: dict[str, float]) -> float:
    source_parts = split_source_parts(source_path)
    has_menu_name = bool(menu_name.strip())
    menu_text = effective_menu_text(source_path, menu_name)
    menu_segments = effective_menu_segments(source_path, menu_name)
    menu_tokens = tokenize(menu_text)
    menu_tail_tokens = tokenize(" ".join(menu_segments[-2:]))
    menu_head_tokens = tokenize(" ".join(menu_segments[:2]))
    source_context_tokens = tokenize(source_match_text(source_path))
    file_tokens = tokenize(Path(source_parts[-1]).stem if source_parts else "")
    source_markers = extract_markers(source_path, menu_name)

    main_overlap = weighted_overlap(menu_tokens, candidate["all_tokens"], idf)
    tail_overlap = weighted_overlap(menu_tail_tokens, candidate["all_tokens"], idf)
    head_overlap = weighted_overlap(menu_head_tokens, candidate["all_tokens"], idf)
    file_overlap = weighted_overlap(file_tokens, candidate["all_tokens"], idf)
    source_overlap = weighted_overlap(source_context_tokens, candidate["all_tokens"], idf)
    menu_segment_score = segment_score(menu_segments, candidate, idf)
    order_score = seq_token_score(menu_tokens, candidate["keyword_tokens"] + candidate["path_tokens"] + candidate["title_tokens"])
    phrase_ratio = SequenceMatcher(None, " ".join(menu_tokens), candidate["full_phrase"]).ratio() if menu_tokens else 0.0
    leaf_ratio = SequenceMatcher(None, " ".join(file_tokens), candidate["leaf_phrase"]).ratio() if file_tokens else 0.0
    marker_score = marker_alignment(source_markers, candidate["markers"])
    penalty = mismatch_penalty(source_markers, candidate["markers"])
    bonus = structural_bonus(source_path, candidate)

    if has_menu_name:
        score = (
            0.18 * main_overlap
            + 0.10 * head_overlap
            + 0.10 * tail_overlap
            + 0.16 * file_overlap
            + 0.16 * source_overlap
            + 0.10 * menu_segment_score
            + 0.05 * order_score
            + 0.03 * phrase_ratio
            + 0.02 * leaf_ratio
            + 0.18 * marker_score
            + bonus
            - penalty
        )
    else:
        score = (
            0.12 * main_overlap
            + 0.06 * head_overlap
            + 0.10 * tail_overlap
            + 0.22 * file_overlap
            + 0.22 * source_overlap
            + 0.11 * menu_segment_score
            + 0.05 * order_score
            + 0.02 * phrase_ratio
            + 0.04 * leaf_ratio
            + 0.18 * marker_score
            + bonus
            - penalty
        )
    return max(0.0, min(1.0, score))


def shortlist_candidates(
    source_path: str,
    menu_name: str,
    candidates: list[dict],
    idf: dict[str, float],
    indexes: dict[str, dict],
) -> list[dict]:
    source_parts = split_source_parts(source_path)
    source_root = source_root_key(source_parts)
    allowed_roots = ROOT_MAP.get(source_root, ())
    if not allowed_roots:
        return candidates

    query_tokens = tokenize(effective_menu_text(source_path, menu_name))
    query_tokens += tokenize(Path(source_parts[-1]).stem if source_parts else "")
    query_tokens += tokenize(source_match_text(source_path))
    source_markers = extract_markers(source_path, menu_name)
    query_unique = set(query_tokens)

    ranked_tokens = sorted(set(query_tokens), key=lambda token: idf.get(token, 0.0), reverse=True)
    collected: set[int] = set()

    for root in allowed_roots:
        token_index = indexes["tokens"].get(root, {})
        marker_index = indexes["markers"].get(root, {})

        for token in ranked_tokens[:8]:
            collected.update(token_index.get(token, set()))

        for marker in source_markers:
            collected.update(marker_index.get(marker, set()))

    if not collected:
        for root in allowed_roots:
            collected.update(indexes["roots"].get(root, []))
    elif len(collected) < 40:
        for root in allowed_roots:
            token_index = indexes["tokens"].get(root, {})
            for token in ranked_tokens[8:16]:
                collected.update(token_index.get(token, set()))

    shortlisted = [candidates[idx] for idx in collected]
    if len(shortlisted) <= 80:
        return shortlisted

    def rough_score(candidate: dict) -> float:
        overlap = sum(idf.get(token, 0.0) for token in query_unique if token in candidate["token_set"])
        markers = sum(MARKER_WEIGHTS.get(marker, 0.0) for marker in source_markers if marker in candidate["markers"])
        return overlap + 1.5 * markers

    shortlisted.sort(key=rough_score, reverse=True)
    return shortlisted[:80]


def enrich_rows(
    root_dir: Path,
    input_csv_path: Path,
    output_csv_path: Path,
    candidates: list[dict],
    idf: dict[str, float],
    indexes: dict[str, dict],
) -> dict[str, int]:
    with input_csv_path.open("r", encoding="utf-8-sig", newline="") as handle:
        rows = list(csv.reader(handle, delimiter=";"))

    enriched_rows: list[list[str]] = []
    matched = 0
    unmatched = 0
    description_cache: dict[str, str] = {}

    for row in rows:
        if len(row) < 2:
            enriched_rows.append(row)
            continue

        source_path = row[0]
        menu_name = row[1]
        scoped_candidates = shortlist_candidates(source_path, menu_name, candidates, idf, indexes)

        best_score = -1.0
        best_candidate = None
        for candidate in scoped_candidates:
            score = score_candidate(source_path, menu_name, candidate, idf)
            if score > best_score:
                best_score = score
                best_candidate = candidate

        url = ""
        description = ""
        if best_candidate and best_score >= THRESHOLD:
            url = BASE_URL + best_candidate["path"]
            relative_doc_path = best_candidate["path"].lstrip("/").replace("/", "\\")
            if relative_doc_path not in description_cache:
                description_cache[relative_doc_path] = extract_description_text(root_dir / relative_doc_path)
            description = description_cache[relative_doc_path]
            matched += 1
        else:
            unmatched += 1

        enriched_rows.append([row[0], row[1], url, f"{best_score:.4f}", description])

    with output_csv_path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.writer(handle, delimiter=";")
        writer.writerows(enriched_rows)

    return {"matched": matched, "unmatched": unmatched, "total": matched + unmatched}


def main() -> None:
    root = Path(__file__).resolve().parent
    csv_path = root / "final.csv"
    output_path = csv_path
    manifest_path = root / "search-manifest.json"

    try:
        with csv_path.open("a", encoding="utf-8"):
            pass
    except PermissionError:
        output_path = root / "final_enriched.csv"

    candidates, idf = build_candidates(manifest_path)
    indexes = build_indexes(candidates)
    stats = enrich_rows(root, csv_path, output_path, candidates, idf, indexes)
    print(f"Enriched {stats['total']} rows")
    print(f"Matched: {stats['matched']}")
    print(f"Unmatched: {stats['unmatched']}")
    print(f"Output: {output_path.name}")


if __name__ == "__main__":
    main()
