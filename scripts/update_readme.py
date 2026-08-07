"""Update the generated notebook catalogue in README.md."""

from __future__ import annotations

import re
from pathlib import Path
from urllib.parse import quote

import nbformat


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOKS_DIR = ROOT / "notebooks"
README_PATH = ROOT / "README.md"
START_MARKER = "<!-- NOTEBOOK_TABLE_START -->"
END_MARKER = "<!-- NOTEBOOK_TABLE_END -->"
FIELDS = ("Description", "Level", "Tags")
GITHUB_REPOSITORY = "m-a-r-o-u/educational-notebooks"
DEFAULT_BRANCH = "main"
GITHUB_BASE_URL = "https://github.com"
COLAB_BASE_URL = "https://colab.research.google.com/github"


def first_markdown_cell(notebook: nbformat.NotebookNode) -> str:
    """Return the contents of the first Markdown cell, if one exists."""
    for cell in notebook.cells:
        if cell.cell_type == "markdown":
            return cell.source
    return ""


def topic_from(source: str, path: Path) -> str:
    """Read the first Markdown heading, falling back to the filename."""
    for line in source.splitlines():
        match = re.match(r"^\s*#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            return match.group(1).strip()
    return path.stem.replace("-", " ").replace("_", " ").title()


def metadata_from(source: str) -> dict[str, str]:
    """Extract supported metadata fields from a Markdown cell."""
    metadata = {field: "" for field in FIELDS}
    pattern = re.compile(
        r"^\s*\*\*(Description|Level|Tags):\*\*\s*(.*?)\s*$",
        re.IGNORECASE,
    )
    field_names = {field.lower(): field for field in FIELDS}
    for line in source.splitlines():
        match = pattern.match(line)
        if match:
            metadata[field_names[match.group(1).lower()]] = match.group(2)
    return metadata


def table_cell(value: str) -> str:
    """Escape content that would break a Markdown table row."""
    return value.replace("|", "\\|").replace("\r", " ").replace("\n", " ")


def notebook_rows() -> list[dict[str, str]]:
    """Collect catalogue information for every notebook."""
    rows = []
    for path in NOTEBOOKS_DIR.rglob("*.ipynb"):
        relative = path.relative_to(ROOT)
        below_notebooks = path.relative_to(NOTEBOOKS_DIR)
        category = below_notebooks.parts[0] if len(below_notebooks.parts) > 1 else ""

        notebook = nbformat.read(path, as_version=4)
        markdown = first_markdown_cell(notebook)
        metadata = metadata_from(markdown)
        notebook_path = quote(relative.as_posix(), safe="/")
        rows.append(
            {
                "category": category,
                "topic": topic_from(markdown, path),
                "github_link": (
                    f"{GITHUB_BASE_URL}/{GITHUB_REPOSITORY}/blob/"
                    f"{DEFAULT_BRANCH}/{notebook_path}"
                ),
                "colab_link": (
                    f"{COLAB_BASE_URL}/{GITHUB_REPOSITORY}/blob/"
                    f"{DEFAULT_BRANCH}/{notebook_path}"
                ),
                **{field.lower(): value for field, value in metadata.items()},
            }
        )

    return sorted(rows, key=lambda row: (row["category"].casefold(), row["topic"].casefold()))


def render_table(rows: list[dict[str, str]]) -> str:
    """Render notebook information as a Markdown table."""
    lines = [
        "| Category | Topic | Notebook | Level | Description | Tags |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for row in rows:
        values = (
            table_cell(row["category"]),
            table_cell(row["topic"]),
            f'[GitHub]({row["github_link"]}) or [Colab]({row["colab_link"]})',
            table_cell(row["level"]),
            table_cell(row["description"]),
            table_cell(row["tags"]),
        )
        lines.append("| " + " | ".join(values) + " |")
    return "\n".join(lines)


def update_readme() -> None:
    """Replace only the generated section of README.md."""
    readme = README_PATH.read_text(encoding="utf-8")
    start = readme.find(START_MARKER)
    end = readme.find(END_MARKER)
    if start == -1 or end == -1 or end < start:
        raise RuntimeError("README.md does not contain valid notebook table markers")

    before = readme[: start + len(START_MARKER)]
    after = readme[end:]
    README_PATH.write_text(
        f"{before}\n{render_table(notebook_rows())}\n{after}", encoding="utf-8"
    )


if __name__ == "__main__":
    update_readme()
