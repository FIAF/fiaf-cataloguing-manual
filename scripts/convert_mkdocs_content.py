#!/usr/bin/env python3
"""Convert FIAF Markdown source to MkDocs content tree.

MkDocs-specific conversion:
- Output root: docs/
- Index filenames: index.md (not _index.md)
- Callout format: MkDocs Material admonitions instead of GitHub-style alerts
- Frontmatter: title only (no weight; ordering via explicit nav in mkdocs.yml)
- Diagram copy target: docs/diagrams/
"""
import argparse
import re
import shutil
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]

# Maps source folder names to output paths relative to docs/.
# Sources not listed here are skipped.
SOURCE_FOLDER_MAP: Dict[str, str] = {
    "00_preliminary": "preliminary",
    "01_moving_image_works": "works",
    "02_moving_image_variants": "variants",
    "03_moving_image_manifestations": "manifestations",
    "04a_moving_image_items": "items",
    "04b_boundaries": "boundaries",
    "06_moving_image_agents": "agents",
    "07_moving_image_events": "events",
    "08_moving_image_other_relationships": "other-relationships",
    "09_appendix_01": "appendices/titles",
    "10_appendix_02": "appendices/cataloguers-notes",
    "12_appendix_04": "appendices/value-lists",
    "13_appendix_05": "appendices/aggregates",
    "16_appendix_08": "appendices/element-comparison",
    "17_appendix_09": "appendices/rights",
    "18_appendix_10": "appendices/record-examples",
    "19_appendix_11": "appendices/bibliography",
    "20_appendix_12": "appendices/element-list",
}


@dataclass
class LabelInfo:
    title: str
    url: str
    anchor: str


class Footnotes:
    def __init__(self) -> None:
        self._notes: List[str] = []

    def add(self, text: str) -> str:
        self._notes.append(text.strip())
        return f"[^{len(self._notes)}]"

    def render(self) -> str:
        if not self._notes:
            return ""
        lines = ["", ""]
        for i, note in enumerate(self._notes, start=1):
            lines.append(f"[^{i}]: {note}")
        return "\n".join(lines) + "\n"


def split_frontmatter(text: str) -> Tuple[str, str]:
    if not text.startswith("---\n"):
        return "", text
    end = text.find("\n---", 4)
    if end == -1:
        return "", text
    end = text.find("\n", end + 4)
    if end == -1:
        return "", text
    fm = text[: end + 1]
    body = text[end + 1 :]
    return fm, body


def normalize_label(label: str) -> str:
    return label.strip().replace(":", "-")


def dest_to_url(dest_path: Path) -> str:
    rel = dest_path.relative_to(ROOT / "markdown")
    if rel.name == "index.md":
        rel = rel.parent
    else:
        rel = rel.with_suffix("")
    return "/" + "/".join(rel.parts) + "/"


def slugify(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    text = re.sub(r"-{2,}", "-", text)
    return text.strip("-") or "section"


def iter_sections(lines: List[str]) -> List[Tuple[str, str, Optional[str], Optional[str], int, int]]:
    sections: List[Tuple[str, str, Optional[str], Optional[str], int, int]] = []
    i = 0
    header_re = re.compile(
        r"^\s*\\(section|subsection|subsubsection|paragraph|subparagraph)\*?(?:\[(?P<toc>[^\]]+)\])?\{?(?P<rest>.*)$"
    )
    label_re = re.compile(r"\\label\{([^}]+)\}")
    foot_re = re.compile(r"\\footnote\s*\{((?:[^{}]|\{[^{}]*\})*)\}")
    while i < len(lines):
        line = lines[i]
        m = header_re.match(line)
        if not m:
            i += 1
            continue
        level = m.group(1)
        title = m.group("toc") or m.group("rest").strip()
        # Extract \label{...} if it appears inline on the same header line
        inline_label = label_re.search(title)
        if inline_label:
            label = inline_label.group(1)
            title = title[: inline_label.start()].strip()
        else:
            label = None
        title = title.rstrip("}").strip().rstrip("\\")
        footnote = None
        start = i
        end = i + 1
        j = i + 1
        while j < len(lines):
            check = lines[j]
            if label_re.search(check):
                label = label_re.search(check).group(1)
                end = j + 1
                j += 1
                continue
            if foot_re.search(check):
                footnote = foot_re.search(check).group(1)
                end = j + 1
                j += 1
                continue
            if check.strip() == "}":
                end = j + 1
                j += 1
                continue
            if check.strip() == "":
                end = j + 1
                j += 1
                continue
            if header_re.match(check):
                break
            break
        sections.append((level, title, label, footnote, start, end))
        i = end
    return sections


def convert_sections(lines: List[str], footnotes: Footnotes) -> List[str]:
    output: List[str] = []
    sections = iter_sections(lines)
    idx = 0
    sec_idx = 0
    level_map = {
        "section": 2,
        "subsection": 3,
        "subsubsection": 4,
        "paragraph": 5,
        "subparagraph": 6,
    }
    while idx < len(lines):
        if sec_idx < len(sections) and idx == sections[sec_idx][4]:
            level, title, label, footnote, start, end = sections[sec_idx]
            hashes = "#" * level_map[level]
            anchor = None
            if label:
                anchor = normalize_label(label)
                output.append(f'<a id="{anchor}"></a>')
            if footnote:
                title = f"{title}{footnotes.add(footnote)}"
            output.append(f"{hashes} {title}".rstrip())
            idx = end
            sec_idx += 1
            continue
        output.append(lines[idx])
        idx += 1
    return output


def convert_latex_inline(text: str) -> str:
    """Convert inline LaTeX formatting commands to Markdown equivalents."""
    text = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", text)
    text = re.sub(r"\\textit\{([^}]*)\}", r"*\1*", text)
    text = re.sub(r"\\emph\{([^}]*)\}", r"*\1*", text)
    # LaTeX special character escapes
    text = text.replace("\\&", "&")
    text = text.replace("\\_", "_")
    # LaTeX grouping braces wrapping square-bracket content: {[...]} → [...]
    text = re.sub(r"\{(\[[^\]]*\])\}", r"\1", text)
    return text


# Patterns that look like 2-space-indented paragraphs but are NOT standalone
# examples: lettered list items (a. / a)), roman numeral items (i. / iv)),
# numbered items (1. / 1)), and bare "Example(s):" labels.
_INDENTED_NON_EXAMPLE_RE = re.compile(
    r"^  ("
    r"[a-zA-Z][.)]\s"            # lettered: "a. " or "a) "
    r"|[ivxlcdmIVXLCDM]+[.)]\s"  # roman numerals: "i. " or "iv) "
    r"|\d+[.)]\s"                 # numbered: "1. " or "1) "
    r"|Examples?:\s*$"            # bare label only
    r")"
)


def convert_indented_examples(text: str) -> str:
    """Convert freestanding 2-space-indented paragraphs to example admonitions.

    Some example content in the LaTeX source was written with 2-space leading
    indentation but without tcolorbox wrappers.  After pandoc conversion these
    appear as plain indented paragraphs.  A paragraph qualifies when:
      - its first line starts with exactly 2 spaces followed by a non-space, AND
      - it is preceded by a blank line (i.e. it starts a new paragraph), AND
      - it does not match the exclusion patterns above (list items, labels).
    """
    lines = text.split("\n")
    result: List[str] = []
    i = 0
    while i < len(lines):
        line = lines[i]
        prev_blank = not result or result[-1].strip() == ""
        if (
            prev_blank
            and re.match(r"^  \S", line)
            and not _INDENTED_NON_EXAMPLE_RE.match(line)
        ):
            # Collect all consecutive non-blank lines as one example block.
            para: List[str] = []
            while i < len(lines) and lines[i].strip():
                para.append(lines[i])
                i += 1
            result.append('!!! example "Example"')
            for pline in para:
                result.append("    " + pline.lstrip())
        else:
            result.append(line)
            i += 1
    return "\n".join(result)


def convert_tcolorbox(text: str) -> str:
    """Convert LaTeX tcolorbox blocks to MkDocs Material admonitions."""
    def _replace(match: re.Match) -> str:
        block = match.group(1)
        if "\\begin{tcolorbox}" not in block:
            return match.group(0)
        inner = re.sub(r".*?\\begin\{tcolorbox\}", "", block, flags=re.S)
        inner = re.sub(r"\\end\{tcolorbox\}.*", "", inner, flags=re.S)
        lines = []
        for line in inner.strip().splitlines():
            line = re.sub(r"\\indent\\hspace\{[^}]+\}\s*", "", line)
            line = line.replace("\\\\", "<br/>")
            line = convert_latex_inline(line)
            lines.append(line)
        if not lines:
            return '!!! example "Example"\n'
        # MkDocs Material admonition: 4-space indent
        result_lines = ['!!! example "Example"']
        for line in lines:
            if line.strip():
                result_lines.append("    " + line)
            else:
                result_lines.append("")
        return "\n".join(result_lines)

    return re.sub(r"```\{=latex\}\s*\n(.*?)```", _replace, text, flags=re.S)


def convert_xltabular(text: str) -> str:
    def _convert_block(match: re.Match) -> str:
        block = match.group(0)
        inner = re.sub(r"\\begin\{xltabular\}.*?\n", "", block, flags=re.S)
        inner = re.sub(r"\\end\{xltabular\}", "", inner, flags=re.S)
        lines = [l.strip() for l in inner.splitlines()]
        rows: List[List[str]] = []
        current = ""
        for line in lines:
            if not line or line.startswith("\\hline") or line.startswith("\\setlength"):
                continue
            current = f"{current} {line}".strip()
            if current.endswith("\\\\"):
                row = current[:-2].strip()
                cells = [c.strip() for c in row.split("&")]
                rows.append(cells)
                current = ""
        if current:
            cells = [c.strip() for c in current.split("&")]
            rows.append(cells)
        if not rows:
            return ""
        def clean_cell(cell: str) -> str:
            cell = re.sub(r"\\textbf\{([^}]*)\}", r"**\1**", cell)
            cell = re.sub(r"\\cellcolor\{[^}]*\}", "", cell)
            cell = cell.replace("\\linebreak", "<br/>")
            cell = re.sub(r"\\begin\{tabitemize\}\s*", "", cell)
            cell = re.sub(r"\\end\{tabitemize\}\s*", "", cell)
            cell = re.sub(r"\\item\s*", "<br/>- ", cell)
            cell = cell.replace("|", "\\|")
            return cell.strip()
        rows = [[clean_cell(c) for c in row] for row in rows]
        header = rows[0]
        body = rows[1:] if len(rows) > 1 else []
        lines_out = []
        lines_out.append("| " + " | ".join(header) + " |")
        lines_out.append("| " + " | ".join(["---"] * len(header)) + " |")
        for row in body:
            lines_out.append("| " + " | ".join(row) + " |")
        return "\n".join(lines_out)

    return re.sub(r"\\begin\{xltabular\}.*?\\end\{xltabular\}", _convert_block, text, flags=re.S)


def process_outside_fences(text: str, fn) -> str:
    parts = re.split(r"(```.*?```)", text, flags=re.S)
    for i, part in enumerate(parts):
        if part.startswith("```"):
            continue
        parts[i] = fn(part)
    return "".join(parts)


def convert_footnotes(text: str, footnotes: Footnotes) -> str:
    def repl_latex(match: re.Match) -> str:
        return footnotes.add(match.group(1))

    # Allow one level of nested braces so \nameref{} inside \footnote{} is captured
    text = re.sub(r"\\footnote\s*\{((?:[^{}]|\{[^{}]*\})*)\}", repl_latex, text)

    # Parse ^[...] with a bracket-balanced scanner so that nested brackets
    # inside footnote content (e.g. Markdown links like [text](url)) are
    # captured correctly instead of truncating at the first ].
    result: List[str] = []
    i = 0
    while i < len(text):
        if text[i] == "^" and i + 1 < len(text) and text[i + 1] == "[":
            depth = 1
            j = i + 2
            while j < len(text) and depth > 0:
                if text[j] == "[":
                    depth += 1
                elif text[j] == "]":
                    depth -= 1
                j += 1
            if depth == 0:
                content = text[i + 2 : j - 1]
                result.append(footnotes.add(content))
                i = j
                continue
        result.append(text[i])
        i += 1
    return "".join(result)


def convert_nameref(text: str, label_map: Dict[str, LabelInfo]) -> str:
    def repl(match: re.Match) -> str:
        label = match.group(1)
        info = label_map.get(label)
        anchor = normalize_label(label)
        if not info:
            return f"[{label}](#{anchor})"
        if info.anchor:
            return f"[{info.title}]({info.url}#{info.anchor})"
        return f"[{info.title}]({info.url})"

    return re.sub(r"\\nameref\{([^}]+)\}", repl, text)


def convert_text(
    raw: str,
    label_map: Dict[str, LabelInfo],
    frontmatter: Optional[str],
) -> str:
    _, raw = split_frontmatter(raw)
    raw = raw.replace("/app/src/diagrams/", "/diagrams/")
    raw = re.sub(r"^\s*\\newpage\s*$", "", raw, flags=re.M)
    raw = re.sub(r"^\s*\\tableofcontents\s*$", "", raw, flags=re.M)
    raw = re.sub(r"^\s*\\appendix\s*$", "", raw, flags=re.M)
    raw = re.sub(r"^\s*\\setlength\\extrarowheight.*$", "", raw, flags=re.M)
    # Strip standalone LaTeX font-size commands that have no web equivalent
    raw = re.sub(r"^\s*\\(?:tiny|scriptsize|footnotesize|small|normalsize|large|Large|LARGE|huge|Huge)\s*$", "", raw, flags=re.M)
    # Convert Pandoc image-width attributes {width=Npx} to MkDocs attr_list syntax { width="N" }
    raw = re.sub(r"\{width=(\d+)px\}", r'{ width="\1" }', raw)

    raw = convert_tcolorbox(raw)
    raw = convert_xltabular(raw)
    raw = process_outside_fences(raw, convert_indented_examples)
    raw = process_outside_fences(raw, convert_latex_inline)

    lines = raw.splitlines()
    footnotes = Footnotes()
    lines = convert_sections(lines, footnotes)

    # If the first heading (any level) matches the frontmatter title, drop it
    # (and its anchor).  Subsection pages start at H3, not H2, so we match
    # any heading level rather than only H2.
    fm_title = None
    if frontmatter:
        m = re.search(r"^title:\s*(.+)$", frontmatter, flags=re.M)
        if m:
            fm_title = m.group(1).strip()
    removed_level = 0
    if fm_title:
        for idx, line in enumerate(lines):
            m = re.match(r"^(#{2,}) (.+)", line)
            if m:
                heading = m.group(2).strip()
                if heading == fm_title:
                    removed_level = len(m.group(1))
                    if idx > 0 and lines[idx - 1].startswith("<a id="):
                        lines.pop(idx - 1)
                        idx -= 1
                    lines.pop(idx)
                break

    if removed_level:
        # Demote by (removed_level - 1) so the next heading level becomes H2.
        shift = removed_level - 1

        def demote(line: str) -> str:
            m = re.match(r"^(#{2,}) ", line)
            if m:
                current = len(m.group(1))
                new_level = max(2, current - shift)
                return "#" * new_level + line[current:]
            return line

        lines = [demote(line) for line in lines]
    body = "\n".join(lines)

    body = process_outside_fences(body, lambda t: convert_nameref(t, label_map))
    body = process_outside_fences(body, lambda t: convert_footnotes(t, footnotes))
    # Resolve any \nameref{} embedded inside footnote content
    for i, note in enumerate(footnotes._notes):
        footnotes._notes[i] = convert_nameref(note, label_map)
    body = body.strip() + footnotes.render()

    if frontmatter is None:
        frontmatter = ""
    return frontmatter + body + "\n"


def extract_labels_from_block(block: str, dest: Path) -> Dict[str, LabelInfo]:
    lines = block.splitlines()
    labels: Dict[str, LabelInfo] = {}
    sections = iter_sections(lines)
    if not sections:
        return labels
    first_level, first_title, first_label, _footnote, _s, _e = sections[0]
    for level, title, label, _footnote, _start, _end in sections:
        if not label:
            continue
        anchor = None
        if label != first_label or level != "section":
            anchor = normalize_label(label)
        labels[label] = LabelInfo(
            title=title,
            url=dest_to_url(dest),
            anchor=anchor,
        )
    return labels


def build_frontmatter(title: str) -> str:
    """Build MkDocs frontmatter with title only (no weight)."""
    return f"---\ntitle: {title}\n---\n"


def build_chapter_sources() -> List[Tuple[Path, str]]:
    """Return (source_path, output_subfolder) for each mapped source folder."""
    results = []
    for src in sorted((ROOT / "source_pdf_markdown").glob("*/en.md")):
        folder = src.parent.name
        if folder in SOURCE_FOLDER_MAP:
            results.append((src, SOURCE_FOLDER_MAP[folder]))
    return results


def copy_diagrams() -> None:
    src_dir = ROOT / "src" / "diagrams"
    if not src_dir.exists():
        return
    dest_dir = ROOT / "markdown" / "diagrams"
    dest_dir.mkdir(parents=True, exist_ok=True)
    allowed = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
    for path in src_dir.iterdir():
        if not path.is_file():
            continue
        if path.suffix.lower() not in allowed:
            continue
        shutil.copy2(path, dest_dir / path.name)


def split_sections(text: str) -> Tuple[str, List[str]]:
    lines = text.splitlines()
    section_re = re.compile(r"^\s*\\subsection\*?(?:\[[^\]]+\])?\{")
    starts = [i for i, line in enumerate(lines) if section_re.match(line)]
    if not starts:
        return text, []
    preamble = "\n".join(lines[: starts[0]]).strip()
    blocks = []
    for idx, start in enumerate(starts):
        end = starts[idx + 1] if idx + 1 < len(starts) else len(lines)
        blocks.append("\n".join(lines[start:end]).strip())
    return preamble, blocks


def derive_section_title(block: str) -> Tuple[str, Optional[str]]:
    lines = block.splitlines()
    sections = iter_sections(lines)
    if not sections:
        return "Section", None
    _level, title, label, _footnote, _start, _end = sections[0]
    return title, label


def derive_chapter_title(body: str) -> Tuple[str, Optional[str]]:
    lines = body.splitlines()
    sections = iter_sections(lines)
    for level, title, label, _footnote, _start, _end in sections:
        if level == "section":
            return title, label
    if sections:
        return sections[0][1], sections[0][2]
    return "Section", None


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert FIAF Markdown to MkDocs content.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files.")
    args = parser.parse_args()

    sources = build_chapter_sources()
    docs_root = ROOT / "markdown"

    pages: List[Tuple[Path, str, str]] = []
    label_map: Dict[str, LabelInfo] = {}

    for src, out_subfolder in sources:
        if not src.exists():
            raise FileNotFoundError(src)

        raw = src.read_text(encoding="utf-8")
        _, body = split_frontmatter(raw)
        preamble, blocks = split_sections(body)
        chapter_title, chapter_label = derive_chapter_title(body)

        if blocks:
            first_block = blocks[0]
            index_raw = "\n\n".join([preamble, first_block]).strip()
            fm = build_frontmatter(chapter_title)
            index_dest = docs_root / out_subfolder / "index.md"
            pages.append((index_dest, fm, index_raw))
            new_labels = extract_labels_from_block(index_raw, index_dest)
            for key, val in new_labels.items():
                if key in label_map:
                    print(f"Warning: duplicate label {key} in {src}", flush=True)
                label_map[key] = val
            if chapter_label and chapter_label in label_map:
                label_map[chapter_label].anchor = None

            slug_counts: Dict[str, int] = {}
            for i, block in enumerate(blocks[1:], start=1):
                title, label = derive_section_title(block)
                if label and label.startswith("sec:"):
                    slug = label[len("sec:"):]
                else:
                    slug = slugify(title)
                count = slug_counts.get(slug, 0) + 1
                slug_counts[slug] = count
                if count > 1:
                    slug = f"{slug}-{count}"
                dest = docs_root / out_subfolder / slug / "index.md"
                fm = build_frontmatter(title)
                pages.append((dest, fm, block))
                new_labels = extract_labels_from_block(block, dest)
                for key, val in new_labels.items():
                    if key in label_map:
                        print(f"Warning: duplicate label {key} in {src}", flush=True)
                    label_map[key] = val
        else:
            index_dest = docs_root / out_subfolder / "index.md"
            title = out_subfolder.split("/")[-1].replace("-", " ").title()
            fm = build_frontmatter(title)
            pages.append((index_dest, fm, body.strip()))
            new_labels = extract_labels_from_block(body, index_dest)
            for key, val in new_labels.items():
                if key in label_map:
                    print(f"Warning: duplicate label {key} in {src}", flush=True)
                label_map[key] = val

    outputs: Dict[Path, str] = {}
    for dest, fm, raw in pages:
        content = convert_text(raw, label_map, fm)
        outputs[dest] = content

    if not args.dry_run:
        # Remove old double-nested docs/docs/ directory if present
        old_docs = docs_root / "docs"
        if old_docs.exists() and old_docs.is_dir():
            shutil.rmtree(old_docs)
            print("Removed old docs/docs/ directory.", flush=True)
        copy_diagrams()
        for dest, content in outputs.items():
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")
        print(f"Written {len(outputs)} files.", flush=True)
    else:
        print(f"Dry run: would write {len(outputs)} files.", flush=True)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
