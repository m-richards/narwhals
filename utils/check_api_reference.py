from __future__ import annotations

import inspect
import string
import sys

# ruff: noqa: N806
from collections import deque
from inspect import isfunction
from pathlib import Path
from typing import TYPE_CHECKING, Any

import polars as pl

import narwhals as nw

if TYPE_CHECKING:
    from collections.abc import Iterator

LOWERCASE = tuple(string.ascii_lowercase)

if sys.version_info >= (3, 13):

    def _is_public_method_or_property(obj: Any) -> bool:
        return (isfunction(obj) or isinstance(obj, property)) and obj.__name__.startswith(
            LOWERCASE
        )
else:

    def _is_public_method_or_property(obj: Any) -> bool:
        return (isfunction(obj) and obj.__name__.startswith(LOWERCASE)) or (
            isinstance(obj, property) and obj.fget.__name__.startswith(LOWERCASE)
        )


def iter_api_reference_names(tp: type[Any]) -> Iterator[str]:
    for name, _ in inspect.getmembers(tp, _is_public_method_or_property):
        yield name


def read_documented_members(source: str | Path) -> list[str]:
    MEMBERS_START = "members:\n"
    MEMBERS_PREFIX = "        - "
    DUNDER_PREFIX = "__"
    with open(source) as fd:
        lines = deque(fd.readlines())
    head = lines.popleft()
    while not head.endswith(MEMBERS_START):
        head = lines.popleft()
    while not head.startswith(MEMBERS_PREFIX):
        head = lines.pop()
    lines.append(head)
    all_members = (line.removeprefix(MEMBERS_PREFIX).strip() for line in lines)
    return [m for m in all_members if not m.startswith(DUNDER_PREFIX)]


ret = 0

NAMESPACES = {"dt", "str", "cat", "name", "list", "struct"}
EXPR_ONLY_METHODS = {"over", "map_batches"}
SERIES_ONLY_METHODS = {
    "dtype",
    "implementation",
    "is_empty",
    "is_sorted",
    "hist",
    "item",
    "name",
    "rename",
    "scatter",
    "shape",
    "to_arrow",
    "to_dummies",
    "to_frame",
    "to_list",
    "to_native",
    "to_numpy",
    "to_pandas",
    "to_polars",
    "value_counts",
    "zip_with",
    "__iter__",
    "__contains__",
}
BASE_DTYPES = {
    "NumericType",
    "DType",
    "TemporalType",
    "Literal",
    "OrderedDict",
    "Mapping",
    "Iterable",
}
DIR_API_REF = Path("docs/api-reference")

files = {fp.stem for fp in Path("narwhals").iterdir()}

# Top level functions
top_level_functions = [
    i for i in nw.__all__ if not i[0].isupper() and i[0] != "_" and i not in files
]

documented = read_documented_members(DIR_API_REF / "narwhals.md")

if False:
    extra = missing = NotImplemented


def _walrus_wrapper_extra_9b075e827c2a46cfadcb6aeef94caab2(expr):
    """Wrapper function for assignment expression."""
    global extra
    extra = expr
    return extra


def _walrus_wrapper_extra_a88268b909a049b589fd28e8d721975d(expr):
    """Wrapper function for assignment expression."""
    global extra
    extra = expr
    return extra


def _walrus_wrapper_extra_93b33839ca604ca1847690458e367277(expr):
    """Wrapper function for assignment expression."""
    global extra
    extra = expr
    return extra


def _walrus_wrapper_extra_05fd5d86b22a4fee9e89f19ce5d40dcc(expr):
    """Wrapper function for assignment expression."""
    global extra
    extra = expr
    return extra


def _walrus_wrapper_extra_030df60d45034ab192c934b6c2999d64(expr):
    """Wrapper function for assignment expression."""
    global extra
    extra = expr
    return extra


def _walrus_wrapper_extra_90db61f433b14821aaf826314c3eddd9(expr):
    """Wrapper function for assignment expression."""
    global extra
    extra = expr
    return extra


def _walrus_wrapper_extra_d684b3976ddf43d886eb652ba7c6caae(expr):
    """Wrapper function for assignment expression."""
    global extra
    extra = expr
    return extra


def _walrus_wrapper_missing_1282e276932e4d90ba62a3672c967b1a(expr):
    """Wrapper function for assignment expression."""
    global missing
    missing = expr
    return missing


def _walrus_wrapper_missing_d816c4594f0740eb8ca4d863b9e132cf(expr):
    """Wrapper function for assignment expression."""
    global missing
    missing = expr
    return missing


def _walrus_wrapper_missing_214448f7bcd6488d8506bac8751fdb1c(expr):
    """Wrapper function for assignment expression."""
    global missing
    missing = expr
    return missing


def _walrus_wrapper_missing_2f20f894a02443c3a42cb2becc824719(expr):
    """Wrapper function for assignment expression."""
    global missing
    missing = expr
    return missing


def _walrus_wrapper_missing_515fdc41045b4596a56b79d00e61f4d4(expr):
    """Wrapper function for assignment expression."""
    global missing
    missing = expr
    return missing


def _walrus_wrapper_missing_ea73fef3bfe840399253a91e9c083057(expr):
    """Wrapper function for assignment expression."""
    global missing
    missing = expr
    return missing


def _walrus_wrapper_missing_18517b8768454d4db0d50e1600b12e8c(expr):
    """Wrapper function for assignment expression."""
    global missing
    missing = expr
    return missing


if _walrus_wrapper_missing_1282e276932e4d90ba62a3672c967b1a(set(top_level_functions).difference(documented).difference({"annotations"})):
    print("top-level functions: not documented")  # noqa: T201
    print(missing)  # noqa: T201
    ret = 1
if _walrus_wrapper_extra_9b075e827c2a46cfadcb6aeef94caab2(set(documented).difference(top_level_functions)):
    print("top-level functions: outdated")  # noqa: T201
    print(extra)  # noqa: T201
    ret = 1

# DataFrame methods
dataframe_methods = list(iter_api_reference_names(nw.DataFrame))
documented = read_documented_members(DIR_API_REF / "dataframe.md")
if _walrus_wrapper_missing_d816c4594f0740eb8ca4d863b9e132cf(set(dataframe_methods).difference(documented)):
    print("DataFrame: not documented")  # noqa: T201
    print(missing)  # noqa: T201
    ret = 1
if _walrus_wrapper_extra_a88268b909a049b589fd28e8d721975d(set(documented).difference(dataframe_methods)):
    print("DataFrame: outdated")  # noqa: T201
    print(extra)  # noqa: T201
    ret = 1

# LazyFrame methods
lazyframe_methods = list(iter_api_reference_names(nw.LazyFrame))
documented = read_documented_members(DIR_API_REF / "lazyframe.md")
if _walrus_wrapper_missing_214448f7bcd6488d8506bac8751fdb1c(set(lazyframe_methods).difference(documented)):
    print("LazyFrame: not documented")  # noqa: T201
    print(missing)  # noqa: T201
    ret = 1
if _walrus_wrapper_extra_93b33839ca604ca1847690458e367277(set(documented).difference(lazyframe_methods)):
    print("LazyFrame: outdated")  # noqa: T201
    print(extra)  # noqa: T201
    ret = 1

# Series methods
series_methods = list(iter_api_reference_names(nw.Series))
documented = read_documented_members(DIR_API_REF / "series.md")
if _walrus_wrapper_missing_2f20f894a02443c3a42cb2becc824719(set(series_methods).difference(documented).difference(NAMESPACES)):
    print("Series: not documented")  # noqa: T201
    print(missing)  # noqa: T201
    ret = 1
if _walrus_wrapper_extra_05fd5d86b22a4fee9e89f19ce5d40dcc(set(documented).difference(series_methods)):
    print("Series: outdated")  # noqa: T201
    print(extra)  # noqa: T201
    ret = 1

# Series.{cat, dt, list, str} methods
for namespace in NAMESPACES.difference({"name"}):
    series_ns_methods = [
        i
        for i in dir(getattr(nw.from_native(pl.Series(), series_only=True), namespace))
        if not i[0].isupper() and i[0] != "_"
    ]
    documented = read_documented_members(DIR_API_REF / f"series_{namespace}.md")

    if False:
        extra = missing = NotImplemented

    def _walrus_wrapper_extra_6b5a5482a36344e0a82a06ed8e93887b(expr):
        """Wrapper function for assignment expression."""
        global extra
        extra = expr
        return extra

    def _walrus_wrapper_missing_0876ce92e7654302b44cebee8a0abaa3(expr):
        """Wrapper function for assignment expression."""
        global missing
        missing = expr
        return missing

    if _walrus_wrapper_missing_0876ce92e7654302b44cebee8a0abaa3(set(series_ns_methods).difference(documented)):
        print(f"Series.{namespace}: not documented")  # noqa: T201
        print(missing)  # noqa: T201
        ret = 1
    if _walrus_wrapper_extra_6b5a5482a36344e0a82a06ed8e93887b(set(documented).difference(series_ns_methods)):
        print(f"Series.{namespace}: outdated")  # noqa: T201
        print(extra)  # noqa: T201
        ret = 1

# Expr methods
expr_methods = list(iter_api_reference_names(nw.Expr))
documented = read_documented_members(DIR_API_REF / "expr.md")
if _walrus_wrapper_missing_515fdc41045b4596a56b79d00e61f4d4(set(expr_methods).difference(documented).difference(NAMESPACES)):
    print("Expr: not documented")  # noqa: T201
    print(missing)  # noqa: T201
    ret = 1
if _walrus_wrapper_extra_030df60d45034ab192c934b6c2999d64(set(documented).difference(expr_methods)):
    print("Expr: outdated")  # noqa: T201
    print(extra)  # noqa: T201
    ret = 1

# Expr.{cat, dt, list, name, str} methods
for namespace in NAMESPACES:
    expr_ns_methods = [
        i
        for i in dir(getattr(nw.col("a"), namespace))
        if not i[0].isupper() and i[0] != "_"
    ]
    documented = read_documented_members(DIR_API_REF / f"expr_{namespace}.md")

    if False:
        extra = missing = NotImplemented

    def _walrus_wrapper_extra_6c4c9da8857548af97b45f419a69daf4(expr):
        """Wrapper function for assignment expression."""
        global extra
        extra = expr
        return extra

    def _walrus_wrapper_missing_a8df35b672414859b063354bc331f6db(expr):
        """Wrapper function for assignment expression."""
        global missing
        missing = expr
        return missing

    if _walrus_wrapper_missing_a8df35b672414859b063354bc331f6db(set(expr_ns_methods).difference(documented)):
        print(f"Expr.{namespace}: not documented")  # noqa: T201
        print(missing)  # noqa: T201
        ret = 1
    if _walrus_wrapper_extra_6c4c9da8857548af97b45f419a69daf4(set(documented).difference(expr_ns_methods)):
        print(f"Expr.{namespace}: outdated")  # noqa: T201
        print(extra)  # noqa: T201
        ret = 1

# DTypes
dtypes = [i for i in dir(nw.dtypes) if i[0].isupper() and not i.isupper() and i[0] != "_"]
documented = read_documented_members(DIR_API_REF / "dtypes.md")
if _walrus_wrapper_missing_ea73fef3bfe840399253a91e9c083057(set(dtypes).difference(documented).difference(BASE_DTYPES)):
    print("Dtype: not documented")  # noqa: T201
    print(missing)  # noqa: T201
    ret = 1
if _walrus_wrapper_extra_90db61f433b14821aaf826314c3eddd9(set(documented).difference(dtypes)):
    print("Dtype: outdated")  # noqa: T201
    print(extra)  # noqa: T201
    ret = 1

# Check Expr vs Series
if _walrus_wrapper_missing_18517b8768454d4db0d50e1600b12e8c(set(expr_methods).difference(series_methods).difference(EXPR_ONLY_METHODS)):
    print("In Expr but not in Series")  # noqa: T201
    print(missing)  # noqa: T201
    ret = 1
if _walrus_wrapper_extra_d684b3976ddf43d886eb652ba7c6caae(set(series_methods).difference(expr_methods).difference(SERIES_ONLY_METHODS)):
    print("In Series but not in Expr")  # noqa: T201
    print(extra)  # noqa: T201
    ret = 1

# Check Expr vs Series internal methods
for namespace in NAMESPACES.difference({"name"}):
    expr_internal = [
        i
        for i in dir(getattr(nw.col("a"), namespace))
        if not i[0].isupper() and i[0] != "_"
    ]
    series_internal = [
        i
        for i in dir(getattr(nw.from_native(pl.Series(), series_only=True), namespace))
        if not i[0].isupper() and i[0] != "_"
    ]

    if False:
        extra = missing = NotImplemented

    def _walrus_wrapper_extra_1bd268482a4f4d1491d7ce9269e22f1b(expr):
        """Wrapper function for assignment expression."""
        global extra
        extra = expr
        return extra

    def _walrus_wrapper_missing_1399b555bf51465bb8f53b32ae15bf40(expr):
        """Wrapper function for assignment expression."""
        global missing
        missing = expr
        return missing

    if _walrus_wrapper_missing_1399b555bf51465bb8f53b32ae15bf40(set(expr_internal).difference(series_internal)):
        print(f"In Expr.{namespace} but not in Series.{namespace}")  # noqa: T201
        print(missing)  # noqa: T201
        ret = 1
    if _walrus_wrapper_extra_1bd268482a4f4d1491d7ce9269e22f1b(set(series_internal).difference(expr_internal)):
        print(f"In Series.{namespace} but not in Expr.{namespace}")  # noqa: T201
        print(extra)  # noqa: T201
        ret = 1

sys.exit(ret)
