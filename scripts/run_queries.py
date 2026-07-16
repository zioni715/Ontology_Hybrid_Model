"""Run the six competency/retrieval SPARQL queries on valid PCPO data."""

from __future__ import annotations

import sys

from common import QUERY_DIR, ProjectError, markdown_table, relative, result_table, run_query, valid_graph


def main() -> int:
    try:
        graph = valid_graph()
        query_paths = sorted(QUERY_DIR.glob("Q*.rq"))
        if not query_paths:
            raise ProjectError("No retrieval queries were found in queries/.")

        print(f"Loaded valid PCPO graph: {len(graph)} triples")
        for path in query_paths:
            result = run_query(graph, path)
            headers, rows = result_table(result)
            if not rows:
                raise ProjectError(f"Retrieval query returned no rows: {relative(path)}")
            print(f"\n## {path.stem} ({len(rows)} rows)")
            print(markdown_table(headers, rows))

        print(f"\nExecuted {len(query_paths)} retrieval queries successfully.")
        return 0
    except Exception as exc:
        print(f"[ERROR] {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
