#!/usr/bin/env python3
import argparse
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple


ROOT = Path(__file__).resolve().parents[1]


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
        return f"[^fn{len(self._notes)}]"

    def render(self) -> str:
        if not self._notes:
            return ""
        lines = ["", ""]
        for i, note in enumerate(self._notes, start=1):
            lines.append(f"[^fn{i}]: {note}")
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
    rel = dest_path.relative_to(ROOT / "static" / "content")
    if rel.name == "_index.md":
        rel = rel.parent
    else:
        rel = rel.with_suffix("")
    return "/" + "/".join(rel.parts) + "/"


def iter_sections(lines: List[str]) -> List[Tuple[str, str, Optional[str], Optional[str], int, int]]:
    sections: List[Tuple[str, str, Optional[str], Optional[str], int, int]] = []
    i = 0
    header_re = re.compile(
        r"^\s*\\(section|subsection|subsubsection|paragraph|subparagraph)\*?(?:\[(?P<toc>[^\]]+)\])?\{?(?P<rest>.*)$"
    )
    label_re = re.compile(r"\\label\{([^}]+)\}")
    foot_re = re.compile(r"\\footnote\s*\{([^}]*)\}")
    while i < len(lines):
        line = lines[i]
        m = header_re.match(line)
        if not m:
            i += 1
            continue
        level = m.group(1)
        title = m.group("toc") or m.group("rest").strip()
        title = title.rstrip("}").strip()
        label = None
        footnote = None
        start = i
        end = i + 1
        j = i + 1
        # Scan forward for label/footnote lines that belong to the header.
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


def convert_tcolorbox(text: str) -> str:
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
            lines.append(line)
        return "\n".join(["> " + l for l in lines])

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

    def repl_md(match: re.Match) -> str:
        return footnotes.add(match.group(1))

    text = re.sub(r"\\footnote\s*\{([^}]*)\}", repl_latex, text)
    text = re.sub(r"\^\[([^\]]+)\]", repl_md, text)
    return text


def convert_nameref(text: str, label_map: Dict[str, LabelInfo]) -> str:
    def repl(match: re.Match) -> str:
        label = match.group(1)
        info = label_map.get(label)
        anchor = normalize_label(label)
        if not info:
            return f"[{label}](#{anchor})"
        return f"[{info.title}]({info.url}#{info.anchor})"

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

    raw = convert_tcolorbox(raw)
    raw = convert_xltabular(raw)

    lines = raw.splitlines()
    footnotes = Footnotes()
    lines = convert_sections(lines, footnotes)

    # If the first H2 matches the frontmatter title, drop it (and its anchor).
    fm_title = None
    if frontmatter:
        m = re.search(r"^title:\s*(.+)$", frontmatter, flags=re.M)
        if m:
            fm_title = m.group(1).strip()
    removed_title = False
    if fm_title:
        for idx, line in enumerate(lines):
            if line.startswith("## "):
                heading = line[3:].strip()
                if heading == fm_title:
                    # Remove preceding anchor if present.
                    if idx > 0 and lines[idx - 1].startswith("<a id="):
                        lines.pop(idx - 1)
                        idx -= 1
                    lines.pop(idx)
                    removed_title = True
                break

    if removed_title:
        def demote(line: str) -> str:
            if line.startswith("###### "):
                return "##### " + line[7:]
            if line.startswith("##### "):
                return "#### " + line[6:]
            if line.startswith("#### "):
                return "### " + line[5:]
            if line.startswith("### "):
                return "## " + line[4:]
            return line

        lines = [demote(line) for line in lines]
    body = "\n".join(lines)

    body = process_outside_fences(body, lambda t: convert_nameref(t, label_map))
    body = process_outside_fences(body, lambda t: convert_footnotes(t, footnotes))
    body = body.strip() + footnotes.render()

    if frontmatter is None:
        frontmatter = ""
    return frontmatter + body + "\n"


def extract_labels(src: Path, dest: Path) -> Dict[str, LabelInfo]:
    text = src.read_text(encoding="utf-8")
    _, text = split_frontmatter(text)
    lines = text.splitlines()
    labels: Dict[str, LabelInfo] = {}
    for level, title, label, _footnote, _start, _end in iter_sections(lines):
        if not label:
            continue
        labels[label] = LabelInfo(
            title=title,
            url=dest_to_url(dest),
            anchor=normalize_label(label),
        )
    return labels


def read_frontmatter(dest: Path) -> Optional[str]:
    if not dest.exists():
        return None
    existing = dest.read_text(encoding="utf-8")
    fm, _ = split_frontmatter(existing)
    return fm if fm else ""


def build_chapter_map() -> List[Tuple[Path, Path]]:
    mapping: List[Tuple[Path, Path]] = []
    for src in sorted((ROOT / "markdown").glob("*/en.md")):
        folder = src.parent.name
        dest = ROOT / "static/content/docs" / folder / "_index.md"
        mapping.append((src, dest))
    return mapping


def ensure_frontmatter(dest: Path, src: Path) -> str:
    # Always regenerate frontmatter from source to avoid stale titles/weights.
    text = src.read_text(encoding="utf-8")
    _, text = split_frontmatter(text)
    lines = text.splitlines()
    sections = iter_sections(lines)
    title = sections[0][1] if sections else dest.stem.replace("-", " ").title()
    weight = None
    folder_name = src.parent.name
    m = re.match(r"^(\d+)_", folder_name)
    if m:
        weight = int(m.group(1)) + 1
    fm_lines = ["---", f"title: {title}"]
    if weight is not None:
        fm_lines.append(f"weight: {weight}")
    fm_lines.append("---")
    return "\n".join(fm_lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Convert FIAF Markdown to Hugo content.")
    parser.add_argument("--dry-run", action="store_true", help="Do not write files.")
    args = parser.parse_args()

    mapping = build_chapter_map()

    label_map: Dict[str, LabelInfo] = {}
    for src, dest in mapping:
        if not src.exists():
            raise FileNotFoundError(src)
        new_labels = extract_labels(src, dest)
        for key, val in new_labels.items():
            if key in label_map:
                print(f"Warning: duplicate label {key} in {src}", flush=True)
            label_map[key] = val

    outputs: Dict[Path, str] = {}
    for src, dest in mapping:
        frontmatter = ensure_frontmatter(dest, src)
        raw = src.read_text(encoding="utf-8")
        content = convert_text(raw, label_map, frontmatter)
        outputs[dest] = content

    if not args.dry_run:
        for dest, content in outputs.items():
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(content, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
