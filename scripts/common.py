"""Shared RDF and SPARQL utilities for the PCPO command-line scripts."""

from __future__ import annotations

from pathlib import Path
from typing import Iterable

from rdflib import Graph, URIRef
from rdflib.query import Result


ROOT = Path(__file__).resolve().parents[1]

ONTOLOGY_FILES = (
    ROOT / "ontology" / "schema.ttl",
    ROOT / "ontology" / "classes.ttl",
    ROOT / "ontology" / "properties.ttl",
    ROOT / "ontology" / "code-lists.ttl",
)
VALID_DATA_FILE = ROOT / "data" / "sample-valid.ttl"
INVALID_DATA_FILE = ROOT / "data" / "sample-invalid.ttl"
QUERY_DIR = ROOT / "queries"
VALIDATION_QUERY_DIR = QUERY_DIR / "validation"
REPORT_FILE = ROOT / "reports" / "validation-report.md"


class ProjectError(RuntimeError):
    """Raised when a project file cannot be loaded or queried."""


def relative(path: Path) -> str:
    """Return a stable project-relative path for console and report output."""

    return path.relative_to(ROOT).as_posix()


def load_graph(files: Iterable[Path]) -> Graph:
    """Load Turtle files into one RDFLib graph with contextual errors."""

    graph = Graph()
    for path in files:
        if not path.is_file():
            raise ProjectError(f"Required file does not exist: {relative(path)}")
        try:
            graph.parse(path, format="turtle")
        except Exception as exc:  # RDFLib exposes parser-specific exception types.
            raise ProjectError(f"Failed to parse {relative(path)}: {exc}") from exc
    return graph


def valid_graph() -> Graph:
    """Return the PCPO schema plus valid synthetic example data."""

    return load_graph((*ONTOLOGY_FILES, VALID_DATA_FILE))


def invalid_overlay_graph() -> Graph:
    """Return schema and valid data with intentional invalid cases overlaid."""

    return load_graph((*ONTOLOGY_FILES, VALID_DATA_FILE, INVALID_DATA_FILE))


def run_query(graph: Graph, query_path: Path) -> Result:
    """Execute one SPARQL file and retain its path in any error message."""

    if not query_path.is_file():
        raise ProjectError(f"Query file does not exist: {relative(query_path)}")
    try:
        return graph.query(query_path.read_text(encoding="utf-8"))
    except Exception as exc:
        raise ProjectError(f"Failed to execute {relative(query_path)}: {exc}") from exc


def compact_term(value: object | None) -> str:
    """Render RDF terms compactly for Markdown and console tables."""

    if value is None:
        return ""
    text = str(value)
    namespaces = {
        "https://example.org/pcpo/resource/": "ex:",
        "https://example.org/pcpo#": "pcpo:",
        "http://www.w3.org/2000/01/rdf-schema#": "rdfs:",
    }
    if isinstance(value, URIRef):
        for namespace, prefix in namespaces.items():
            if text.startswith(namespace):
                return prefix + text[len(namespace) :]
    return text.replace("|", "\\|").replace("\n", " ")


def result_table(result: Result, max_rows: int | None = None) -> tuple[list[str], list[list[str]]]:
    """Convert a SELECT result into headers and display-safe rows."""

    headers = [str(variable) for variable in result.vars]
    rows: list[list[str]] = []
    for index, row in enumerate(result):
        if max_rows is not None and index >= max_rows:
            break
        rows.append([compact_term(row.get(variable)) for variable in result.vars])
    return headers, rows


def markdown_table(headers: list[str], rows: list[list[str]]) -> str:
    """Create a Markdown table, including a clear empty-result marker."""

    if not headers:
        return "_No projected variables._"
    header = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join("---" for _ in headers) + " |"
    if not rows:
        empty = "| " + " | ".join("_no rows_" if i == 0 else "" for i in range(len(headers))) + " |"
        return "\n".join((header, separator, empty))
    body = ["| " + " | ".join(row) + " |" for row in rows]
    return "\n".join((header, separator, *body))
