"""Offline regression tests for research figure extraction.

Load only extract_figs from the builder AST to avoid importing optional site
rendering dependencies or executing the publishing workflow.
"""
import ast
import base64
import hashlib
import json
from pathlib import Path
import re
import tempfile
import unittest


BUILDER = Path(__file__).resolve().parents[1] / "scripts" / "build_research_site.py"


def load_extractor():
    tree = ast.parse(BUILDER.read_text(encoding="utf-8"))
    function = next(
        node for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "extract_figs"
    )
    module = ast.fix_missing_locations(ast.Module(body=[function], type_ignores=[]))
    namespace = {
        "Path": Path, "json": json, "base64": base64,
        "hashlib": hashlib, "re": re,
    }
    exec(compile(module, str(BUILDER), "exec"), namespace)
    return namespace["extract_figs"]


class FigureExtractionTests(unittest.TestCase):
    def test_same_named_notebooks_keep_distinct_figures(self):
        extract_figs = load_extractor()
        with tempfile.TemporaryDirectory() as tmp:
            repo = Path(tmp) / "repo"
            site = Path(tmp) / "site"
            for folder, payload in (("first", b"first-image"), ("second", b"second-image")):
                source = repo / folder / "analysis.ipynb"
                source.parent.mkdir(parents=True)
                source.write_text(json.dumps({
                    "cells": [{
                        "cell_type": "code",
                        "metadata": {},
                        "outputs": [{
                            "data": {
                                "image/png": base64.b64encode(payload).decode("ascii")
                            }
                        }]
                    }]
                }), encoding="utf-8")
            figures = extract_figs(repo, site)
            self.assertEqual(len(figures), 2)
            self.assertEqual(len({path.name for path, _ in figures}), 2)
            self.assertEqual(
                {path.read_bytes() for path, _ in figures},
                {b"first-image", b"second-image"},
            )
            self.assertEqual(
                [path.name for path, _ in extract_figs(repo, site)],
                [path.name for path, _ in figures],
            )


if __name__ == "__main__":
    unittest.main()
