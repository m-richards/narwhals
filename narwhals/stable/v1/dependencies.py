from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import cudf
    import dask.dataframe as dd
    import ibis
    import modin.pandas as mpd
    import pandas as pd
    import polars as pl
    import pyarrow as pa
    from typing_extensions import TypeIs


from narwhals.dependencies import (
    IMPORT_HOOKS,
    get_cudf,
    get_dask_dataframe,
    get_ibis,
    get_modin,
    get_numpy,
    get_pandas,
    get_polars,
    get_pyarrow,
    is_into_dataframe,
    is_into_series,
    is_narwhals_dataframe,
    is_narwhals_lazyframe,
    is_narwhals_series,
    is_numpy_array,
    is_pandas_index,
)


def is_pandas_dataframe(df: Any) -> TypeIs[pd.DataFrame]:
    """Check whether `df` is a pandas DataFrame without importing pandas."""

    if False:
        mod = pd = NotImplemented

    def _walrus_wrapper_mod_c92745dbf639467fb8036a37d1ebe5a9(expr):
        """Wrapper function for assignment expression."""
        nonlocal mod
        mod = expr
        return mod

    def _walrus_wrapper_pd_1a84e23c04f6466891a40d5f4756160a(expr):
        """Wrapper function for assignment expression."""
        nonlocal pd
        pd = expr
        return pd

    return ((_walrus_wrapper_pd_1a84e23c04f6466891a40d5f4756160a(get_pandas())) is not None and isinstance(df, pd.DataFrame)) or any(
        (_walrus_wrapper_mod_c92745dbf639467fb8036a37d1ebe5a9(sys.modules.get(module_name, None))) is not None
        and isinstance(df, mod.pandas.DataFrame)
        for module_name in IMPORT_HOOKS
    )


def is_pandas_series(ser: Any) -> TypeIs[pd.Series[Any]]:
    """Check whether `ser` is a pandas Series without importing pandas."""

    if False:
        mod = pd = NotImplemented

    def _walrus_wrapper_mod_d9e0849b20eb4c0daab027fe11503322(expr):
        """Wrapper function for assignment expression."""
        nonlocal mod
        mod = expr
        return mod

    def _walrus_wrapper_pd_304721222ab342bca673adad2d0bf0cd(expr):
        """Wrapper function for assignment expression."""
        nonlocal pd
        pd = expr
        return pd

    return ((_walrus_wrapper_pd_304721222ab342bca673adad2d0bf0cd(get_pandas())) is not None and isinstance(ser, pd.Series)) or any(
        (_walrus_wrapper_mod_d9e0849b20eb4c0daab027fe11503322(sys.modules.get(module_name, None))) is not None
        and isinstance(ser, mod.pandas.Series)
        for module_name in IMPORT_HOOKS
    )


def is_modin_dataframe(df: Any) -> TypeIs[mpd.DataFrame]:
    """Check whether `df` is a modin DataFrame without importing modin."""

    if False:
        mpd = NotImplemented

    def _walrus_wrapper_mpd_591ccc734523448f97bfa83613f2a7d4(expr):
        """Wrapper function for assignment expression."""
        nonlocal mpd
        mpd = expr
        return mpd

    return (_walrus_wrapper_mpd_591ccc734523448f97bfa83613f2a7d4(get_modin())) is not None and isinstance(df, mpd.DataFrame)


def is_modin_series(ser: Any) -> TypeIs[mpd.Series]:
    """Check whether `ser` is a modin Series without importing modin."""

    if False:
        mpd = NotImplemented

    def _walrus_wrapper_mpd_fa7efd3f31d44b7892cb913f897984ab(expr):
        """Wrapper function for assignment expression."""
        nonlocal mpd
        mpd = expr
        return mpd

    return (_walrus_wrapper_mpd_fa7efd3f31d44b7892cb913f897984ab(get_modin())) is not None and isinstance(ser, mpd.Series)


def is_cudf_dataframe(df: Any) -> TypeIs[cudf.DataFrame]:
    """Check whether `df` is a cudf DataFrame without importing cudf."""

    if False:
        cudf = NotImplemented

    def _walrus_wrapper_cudf_5b93e0d08e7744379f2b61e6a5e16482(expr):
        """Wrapper function for assignment expression."""
        nonlocal cudf
        cudf = expr
        return cudf

    return (_walrus_wrapper_cudf_5b93e0d08e7744379f2b61e6a5e16482(get_cudf())) is not None and isinstance(df, cudf.DataFrame)


def is_cudf_series(ser: Any) -> TypeIs[cudf.Series[Any]]:
    """Check whether `ser` is a cudf Series without importing cudf."""

    if False:
        cudf = NotImplemented

    def _walrus_wrapper_cudf_631af69bdddb46718d6b5d91abdf3046(expr):
        """Wrapper function for assignment expression."""
        nonlocal cudf
        cudf = expr
        return cudf

    return (_walrus_wrapper_cudf_631af69bdddb46718d6b5d91abdf3046(get_cudf())) is not None and isinstance(ser, cudf.Series)


def is_dask_dataframe(df: Any) -> TypeIs[dd.DataFrame]:
    """Check whether `df` is a Dask DataFrame without importing Dask."""

    if False:
        dd = NotImplemented

    def _walrus_wrapper_dd_6c687fb873ae4815bb2483affbf8062e(expr):
        """Wrapper function for assignment expression."""
        nonlocal dd
        dd = expr
        return dd

    return (_walrus_wrapper_dd_6c687fb873ae4815bb2483affbf8062e(get_dask_dataframe())) is not None and isinstance(df, dd.DataFrame)


def is_ibis_table(df: Any) -> TypeIs[ibis.Table]:
    """Check whether `df` is a Ibis Table without importing Ibis."""

    if False:
        ibis = NotImplemented

    def _walrus_wrapper_ibis_df09523bf43742cc85ca9314b1d4d3bc(expr):
        """Wrapper function for assignment expression."""
        nonlocal ibis
        ibis = expr
        return ibis

    return (_walrus_wrapper_ibis_df09523bf43742cc85ca9314b1d4d3bc(get_ibis())) is not None and isinstance(df, ibis.expr.types.Table)


def is_polars_dataframe(df: Any) -> TypeIs[pl.DataFrame]:
    """Check whether `df` is a Polars DataFrame without importing Polars."""

    if False:
        pl = NotImplemented

    def _walrus_wrapper_pl_685bc1b5368b4eb7a3cf9794f68d2bc6(expr):
        """Wrapper function for assignment expression."""
        nonlocal pl
        pl = expr
        return pl

    return (_walrus_wrapper_pl_685bc1b5368b4eb7a3cf9794f68d2bc6(get_polars())) is not None and isinstance(df, pl.DataFrame)


def is_polars_lazyframe(df: Any) -> TypeIs[pl.LazyFrame]:
    """Check whether `df` is a Polars LazyFrame without importing Polars."""

    if False:
        pl = NotImplemented

    def _walrus_wrapper_pl_60e322a5e2b54f12aeaf3d433fb04ae9(expr):
        """Wrapper function for assignment expression."""
        nonlocal pl
        pl = expr
        return pl

    return (_walrus_wrapper_pl_60e322a5e2b54f12aeaf3d433fb04ae9(get_polars())) is not None and isinstance(df, pl.LazyFrame)


def is_polars_series(ser: Any) -> TypeIs[pl.Series]:
    """Check whether `ser` is a Polars Series without importing Polars."""

    if False:
        pl = NotImplemented

    def _walrus_wrapper_pl_c77b11a5015a4eed894f4d34ca369f65(expr):
        """Wrapper function for assignment expression."""
        nonlocal pl
        pl = expr
        return pl

    return (_walrus_wrapper_pl_c77b11a5015a4eed894f4d34ca369f65(get_polars())) is not None and isinstance(ser, pl.Series)


def is_pyarrow_chunked_array(ser: Any) -> TypeIs[pa.ChunkedArray[Any]]:
    """Check whether `ser` is a PyArrow ChunkedArray without importing PyArrow."""

    if False:
        pa = NotImplemented

    def _walrus_wrapper_pa_b3707e7d3bb24b94b7614f58bf239bfc(expr):
        """Wrapper function for assignment expression."""
        nonlocal pa
        pa = expr
        return pa

    return (_walrus_wrapper_pa_b3707e7d3bb24b94b7614f58bf239bfc(get_pyarrow())) is not None and isinstance(ser, pa.ChunkedArray)


def is_pyarrow_table(df: Any) -> TypeIs[pa.Table]:
    """Check whether `df` is a PyArrow Table without importing PyArrow."""

    if False:
        pa = NotImplemented

    def _walrus_wrapper_pa_fa7bf6dfb2a54ed78292a7caf8e6df17(expr):
        """Wrapper function for assignment expression."""
        nonlocal pa
        pa = expr
        return pa

    return (_walrus_wrapper_pa_fa7bf6dfb2a54ed78292a7caf8e6df17(get_pyarrow())) is not None and isinstance(df, pa.Table)


def is_pandas_like_dataframe(df: Any) -> bool:
    """Check whether `df` is a pandas-like DataFrame without doing any imports.

    By "pandas-like", we mean: pandas, Modin, cuDF.
    """
    return is_pandas_dataframe(df) or is_modin_dataframe(df) or is_cudf_dataframe(df)


def is_pandas_like_series(ser: Any) -> bool:
    """Check whether `ser` is a pandas-like Series without doing any imports.

    By "pandas-like", we mean: pandas, Modin, cuDF.
    """
    return is_pandas_series(ser) or is_modin_series(ser) or is_cudf_series(ser)


__all__ = [
    "get_cudf",
    "get_ibis",
    "get_modin",
    "get_numpy",
    "get_pandas",
    "get_polars",
    "get_pyarrow",
    "is_cudf_dataframe",
    "is_cudf_series",
    "is_dask_dataframe",
    "is_ibis_table",
    "is_into_dataframe",
    "is_into_series",
    "is_modin_dataframe",
    "is_modin_series",
    "is_narwhals_dataframe",
    "is_narwhals_lazyframe",
    "is_narwhals_series",
    "is_numpy_array",
    "is_pandas_dataframe",
    "is_pandas_index",
    "is_pandas_like_dataframe",
    "is_pandas_like_series",
    "is_pandas_series",
    "is_polars_dataframe",
    "is_polars_lazyframe",
    "is_polars_series",
    "is_pyarrow_chunked_array",
    "is_pyarrow_table",
]
