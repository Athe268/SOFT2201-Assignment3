"""Deselect tests that do not contain an explicit Python ``assert``."""

from __future__ import annotations

import ast
import inspect
import textwrap


def _contains_assert(test_function: object) -> bool:
    try:
        source = inspect.getsource(test_function)
    except (OSError, TypeError):
        return False
    tree = ast.parse(textwrap.dedent(source))
    return any(isinstance(node, ast.Assert) for node in ast.walk(tree))


def pytest_collection_modifyitems(config, items) -> None:
    selected = []
    deselected = []
    for item in items:
        if _contains_assert(getattr(item, "obj", None)):
            selected.append(item)
        else:
            deselected.append(item)
    if deselected:
        config.hook.pytest_deselected(items=deselected)
    items[:] = selected
