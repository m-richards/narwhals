# pandas / Polars / etc. : if a user passes a dataframe from one of these
# libraries, it means they must already have imported the given module.
# So, we can just check sys.modules.
from __future__ import annotations

import sys
from typing import TYPE_CHECKING, Any

if TYPE_CHECKING:
    import cudf
    import dask.dataframe as dd
    import duckdb
    import ibis
    import modin.pandas as mpd
    import pandas as pd
    import polars as pl
    import pyarrow as pa
    import pyspark.sql as pyspark_sql
    from pyspark.sql.connect.dataframe import DataFrame as PySparkConnectDataFrame
    from typing_extensions import TypeGuard, TypeIs

    from narwhals._spark_like.dataframe import SQLFrameDataFrame
    from narwhals.dataframe import DataFrame, LazyFrame
    from narwhals.series import Series
    from narwhals.typing import (
        IntoDataFrameT,
        IntoLazyFrameT,
        IntoSeriesT,
        _1DArray,
        _1DArrayInt,
        _2DArray,
        _NDArray,
        _NumpyScalar,
        _ShapeT,
    )


# We silently allow these but - given that they claim
# to be drop-in replacements for pandas - testing is
# their responsibility.
IMPORT_HOOKS = frozenset(["fireducks"])


def get_polars() -> Any:
    """Get Polars module (if already imported - else return None)."""
    return sys.modules.get("polars", None)


def get_pandas() -> Any:
    """Get pandas module (if already imported - else return None)."""
    return sys.modules.get("pandas", None)


def get_modin() -> Any:
    # pragma: no cover
    """Get modin.pandas module (if already imported - else return None)."""

    if False:
        modin = NotImplemented

    def _walrus_wrapper_modin_9d0295c829e54596baa98f90ad973adb(expr):
        """Wrapper function for assignment expression."""
        nonlocal modin
        modin = expr
        return modin

    if (_walrus_wrapper_modin_9d0295c829e54596baa98f90ad973adb(sys.modules.get("modin", None))) is not None:
        return modin.pandas
    return None


def get_cudf() -> Any:
    """Get cudf module (if already imported - else return None)."""
    return sys.modules.get("cudf", None)


def get_cupy() -> Any:
    """Get cupy module (if already imported - else return None)."""
    return sys.modules.get("cupy", None)


def get_pyarrow() -> Any:  # pragma: no cover
    """Get pyarrow module (if already imported - else return None)."""
    return sys.modules.get("pyarrow", None)


def get_numpy() -> Any:
    """Get numpy module (if already imported - else return None)."""
    return sys.modules.get("numpy", None)


def get_dask() -> Any:
    """Get dask (if already imported - else return None)."""
    return sys.modules.get("dask", None)


def get_dask_dataframe() -> Any:
    """Get dask.dataframe module (if already imported - else return None)."""
    return sys.modules.get("dask.dataframe", None)


def get_duckdb() -> Any:
    """Get duckdb module (if already imported - else return None)."""
    return sys.modules.get("duckdb", None)


def get_ibis() -> Any:
    """Get ibis module (if already imported - else return None)."""
    return sys.modules.get("ibis", None)


def get_dask_expr() -> Any:
    # pragma: no cover
    """Get dask_expr module (if already imported - else return None)."""

    if False:
        dd = NotImplemented

    def _walrus_wrapper_dd_7d441d42fccd49c399ec80c9e1fcbe38(expr):
        """Wrapper function for assignment expression."""
        nonlocal dd
        dd = expr
        return dd

    if (_walrus_wrapper_dd_7d441d42fccd49c399ec80c9e1fcbe38(get_dask_dataframe())) is not None and hasattr(dd, "dask_expr"):
        return dd.dask_expr
    return sys.modules.get("dask_expr", None)


def get_pyspark() -> Any:  # pragma: no cover
    """Get pyspark module (if already imported - else return None)."""
    return sys.modules.get("pyspark", None)


def get_pyspark_sql() -> Any:
    """Get pyspark.sql module (if already imported - else return None)."""
    return sys.modules.get("pyspark.sql", None)


def get_pyspark_connect() -> Any:
    """Get pyspark.sql.connect module (if already imported - else return None)."""
    return sys.modules.get("pyspark.sql.connect", None)


def get_sqlframe() -> Any:
    """Get sqlframe module (if already imported - else return None)."""
    return sys.modules.get("sqlframe", None)


def _raise_if_narwhals_df_or_lf(df: Any) -> None:
    if is_narwhals_dataframe(df) or is_narwhals_lazyframe(df):
        msg = (
            f"You passed a `{type(df)}` to `is_pandas_dataframe`.\n\n"
            "Hint: Instead of e.g. `is_pandas_dataframe(df)`, "
            "did you mean `is_pandas_dataframe(df.to_native())`?"
        )
        raise TypeError(msg)


def _raise_if_narwhals_series(ser: Any) -> None:
    if is_narwhals_series(ser):
        msg = (
            f"You passed a `{type(ser)}` to `is_pandas_series`.\n\n"
            "Hint: Instead of e.g. `is_pandas_series(ser)`, "
            "did you mean `is_pandas_series(ser.to_native())`?"
        )
        raise TypeError(msg)


def is_pandas_dataframe(df: Any) -> TypeIs[pd.DataFrame]:
    """Check whether `df` is a pandas DataFrame without importing pandas.

    Warning:
        This method cannot be called on a Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)

    if False:
        mod = pd = NotImplemented

    def _walrus_wrapper_mod_73d53f770d9045ec9de5d3eddc28cb8d(expr):
        """Wrapper function for assignment expression."""
        nonlocal mod
        mod = expr
        return mod

    def _walrus_wrapper_pd_12018570ef53467884a11b19e848ec4e(expr):
        """Wrapper function for assignment expression."""
        nonlocal pd
        pd = expr
        return pd

    return ((_walrus_wrapper_pd_12018570ef53467884a11b19e848ec4e(get_pandas())) is not None and isinstance(df, pd.DataFrame)) or any(
        (_walrus_wrapper_mod_73d53f770d9045ec9de5d3eddc28cb8d(sys.modules.get(module_name, None))) is not None
        and isinstance(df, mod.pandas.DataFrame)
        for module_name in IMPORT_HOOKS
    )


def is_pandas_series(ser: Any) -> TypeIs[pd.Series[Any]]:
    """Check whether `ser` is a pandas Series without importing pandas.

    Warning:
        This method cannot be called on Narwhals Series.
    """
    _raise_if_narwhals_series(ser)

    if False:
        mod = pd = NotImplemented

    def _walrus_wrapper_mod_7b46ffb5906646d390b864f521287562(expr):
        """Wrapper function for assignment expression."""
        nonlocal mod
        mod = expr
        return mod

    def _walrus_wrapper_pd_ea6823d8829543a6b7167603cac9ac45(expr):
        """Wrapper function for assignment expression."""
        nonlocal pd
        pd = expr
        return pd

    return ((_walrus_wrapper_pd_ea6823d8829543a6b7167603cac9ac45(get_pandas())) is not None and isinstance(ser, pd.Series)) or any(
        (_walrus_wrapper_mod_7b46ffb5906646d390b864f521287562(sys.modules.get(module_name, None))) is not None
        and isinstance(ser, mod.pandas.Series)
        for module_name in IMPORT_HOOKS
    )


def is_pandas_index(index: Any) -> TypeIs[pd.Index[Any]]:
    """Check whether `index` is a pandas Index without importing pandas."""

    if False:
        mod = pd = NotImplemented

    def _walrus_wrapper_mod_c862ddc45aae47da85424b1841103c82(expr):
        """Wrapper function for assignment expression."""
        nonlocal mod
        mod = expr
        return mod

    def _walrus_wrapper_pd_55605018b11b4216a646553cfa848d5d(expr):
        """Wrapper function for assignment expression."""
        nonlocal pd
        pd = expr
        return pd

    return ((_walrus_wrapper_pd_55605018b11b4216a646553cfa848d5d(get_pandas())) is not None and isinstance(index, pd.Index)) or any(
        (_walrus_wrapper_mod_c862ddc45aae47da85424b1841103c82(sys.modules.get(module_name, None))) is not None
        and isinstance(index, mod.pandas.Index)
        for module_name in IMPORT_HOOKS
    )


def is_modin_dataframe(df: Any) -> TypeIs[mpd.DataFrame]:
    """Check whether `df` is a modin DataFrame without importing modin.

    Warning:
        This method cannot be called on a Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)

    if False:
        mpd = NotImplemented

    def _walrus_wrapper_mpd_9257ae0540fe44a8ae40ef6a9db7e311(expr):
        """Wrapper function for assignment expression."""
        nonlocal mpd
        mpd = expr
        return mpd

    return (_walrus_wrapper_mpd_9257ae0540fe44a8ae40ef6a9db7e311(get_modin())) is not None and isinstance(df, mpd.DataFrame)


def is_modin_series(ser: Any) -> TypeIs[mpd.Series]:
    """Check whether `ser` is a modin Series without importing modin.

    Warning:
        This method cannot be called on Narwhals Series.
    """
    _raise_if_narwhals_series(ser)

    if False:
        mpd = NotImplemented

    def _walrus_wrapper_mpd_8220a43dfd114742b20d0f8277ac2bfb(expr):
        """Wrapper function for assignment expression."""
        nonlocal mpd
        mpd = expr
        return mpd

    return (_walrus_wrapper_mpd_8220a43dfd114742b20d0f8277ac2bfb(get_modin())) is not None and isinstance(ser, mpd.Series)


def is_modin_index(index: Any) -> TypeIs[mpd.Index[Any]]:
    # pragma: no cover
    """Check whether `index` is a modin Index without importing modin."""

    if False:
        mpd = NotImplemented

    def _walrus_wrapper_mpd_b1e6513074f34a01ad60283ccfb8a677(expr):
        """Wrapper function for assignment expression."""
        nonlocal mpd
        mpd = expr
        return mpd

    return (_walrus_wrapper_mpd_b1e6513074f34a01ad60283ccfb8a677(get_modin())) is not None and isinstance(index, mpd.Index)


def is_cudf_dataframe(df: Any) -> TypeIs[cudf.DataFrame]:
    """Check whether `df` is a cudf DataFrame without importing cudf.

    Warning:
        This method cannot be called on a Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)

    if False:
        cudf = NotImplemented

    def _walrus_wrapper_cudf_dd67431b2a4c4c59964d0ac557b87102(expr):
        """Wrapper function for assignment expression."""
        nonlocal cudf
        cudf = expr
        return cudf

    return (_walrus_wrapper_cudf_dd67431b2a4c4c59964d0ac557b87102(get_cudf())) is not None and isinstance(df, cudf.DataFrame)


def is_cudf_series(ser: Any) -> TypeIs[cudf.Series[Any]]:
    """Check whether `ser` is a cudf Series without importing cudf.

    Warning:
        This method cannot be called on Narwhals Series.
    """
    _raise_if_narwhals_series(ser)

    if False:
        cudf = NotImplemented

    def _walrus_wrapper_cudf_c52f20fde79445189481618dc26200da(expr):
        """Wrapper function for assignment expression."""
        nonlocal cudf
        cudf = expr
        return cudf

    return (_walrus_wrapper_cudf_c52f20fde79445189481618dc26200da(get_cudf())) is not None and isinstance(ser, cudf.Series)


def is_cudf_index(index: Any) -> TypeIs[cudf.Index]:
    """Check whether `index` is a cudf Index without importing cudf."""

    if False:
        cudf = NotImplemented

    def _walrus_wrapper_cudf_56371c503390484cab7d812e1d8e48bf(expr):
        """Wrapper function for assignment expression."""
        nonlocal cudf
        cudf = expr
        return cudf

    return (_walrus_wrapper_cudf_56371c503390484cab7d812e1d8e48bf(get_cudf())) is not None and isinstance(
        index, cudf.Index
    )  # pragma: no cover


def is_cupy_scalar(obj: Any) -> bool:
    if False:
        cupy = NotImplemented

    def _walrus_wrapper_cupy_b2508f921e7045ea871717623c21b28a(expr):
        """Wrapper function for assignment expression."""
        nonlocal cupy
        cupy = expr
        return cupy

    return (
        (_walrus_wrapper_cupy_b2508f921e7045ea871717623c21b28a(get_cupy())) is not None
        and isinstance(obj, cupy.ndarray)
        and obj.size == 1
    )  # pragma: no cover


def is_dask_dataframe(df: Any) -> TypeIs[dd.DataFrame]:
    """Check whether `df` is a Dask DataFrame without importing Dask.

    Warning:
        This method cannot be called on a Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)

    if False:
        dd = NotImplemented

    def _walrus_wrapper_dd_5cf2ca1503664ff9846b712d4339ad11(expr):
        """Wrapper function for assignment expression."""
        nonlocal dd
        dd = expr
        return dd

    return (_walrus_wrapper_dd_5cf2ca1503664ff9846b712d4339ad11(get_dask_dataframe())) is not None and isinstance(df, dd.DataFrame)


def is_duckdb_relation(df: Any) -> TypeIs[duckdb.DuckDBPyRelation]:
    """Check whether `df` is a DuckDB Relation without importing DuckDB.

    Warning:
        This method cannot be called on Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)

    if False:
        duckdb = NotImplemented

    def _walrus_wrapper_duckdb_a08c241643044aceb9f36aaec8ba9d52(expr):
        """Wrapper function for assignment expression."""
        nonlocal duckdb
        duckdb = expr
        return duckdb

    return (_walrus_wrapper_duckdb_a08c241643044aceb9f36aaec8ba9d52(get_duckdb())) is not None and isinstance(
        df, duckdb.DuckDBPyRelation
    )


def is_ibis_table(df: Any) -> TypeIs[ibis.Table]:
    """Check whether `df` is a Ibis Table without importing Ibis.

    Warning:
        This method cannot be called on Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)

    if False:
        ibis = NotImplemented

    def _walrus_wrapper_ibis_8fc8b89dae7d4124856f34c635a583ea(expr):
        """Wrapper function for assignment expression."""
        nonlocal ibis
        ibis = expr
        return ibis

    return (_walrus_wrapper_ibis_8fc8b89dae7d4124856f34c635a583ea(get_ibis())) is not None and isinstance(df, ibis.expr.types.Table)


def is_polars_dataframe(df: Any) -> TypeIs[pl.DataFrame]:
    """Check whether `df` is a Polars DataFrame without importing Polars.

    Warning:
        This method cannot be called on a Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)

    if False:
        pl = NotImplemented

    def _walrus_wrapper_pl_a290783a51694d498cc792195338c95a(expr):
        """Wrapper function for assignment expression."""
        nonlocal pl
        pl = expr
        return pl

    return (_walrus_wrapper_pl_a290783a51694d498cc792195338c95a(get_polars())) is not None and isinstance(df, pl.DataFrame)


def is_polars_lazyframe(df: Any) -> TypeIs[pl.LazyFrame]:
    """Check whether `df` is a Polars LazyFrame without importing Polars.

    Warning:
        This method cannot be called on Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)

    if False:
        pl = NotImplemented

    def _walrus_wrapper_pl_a2f1592feafd4992bd1ec7e4455519d0(expr):
        """Wrapper function for assignment expression."""
        nonlocal pl
        pl = expr
        return pl

    return (_walrus_wrapper_pl_a2f1592feafd4992bd1ec7e4455519d0(get_polars())) is not None and isinstance(df, pl.LazyFrame)


def is_polars_series(ser: Any) -> TypeIs[pl.Series]:
    """Check whether `ser` is a Polars Series without importing Polars.

    Warning:
        This method cannot be called on Narwhals Series.
    """
    _raise_if_narwhals_series(ser)

    if False:
        pl = NotImplemented

    def _walrus_wrapper_pl_b003c32586424fadb2941e6c62ac177a(expr):
        """Wrapper function for assignment expression."""
        nonlocal pl
        pl = expr
        return pl

    return (_walrus_wrapper_pl_b003c32586424fadb2941e6c62ac177a(get_polars())) is not None and isinstance(ser, pl.Series)


def is_pyarrow_chunked_array(ser: Any) -> TypeIs[pa.ChunkedArray[Any]]:
    """Check whether `ser` is a PyArrow ChunkedArray without importing PyArrow.

    Warning:
        This method cannot be called on Narwhals Series.
    """
    _raise_if_narwhals_series(ser)

    if False:
        pa = NotImplemented

    def _walrus_wrapper_pa_64a3d61c24b24100a10416ee60c44fd7(expr):
        """Wrapper function for assignment expression."""
        nonlocal pa
        pa = expr
        return pa

    return (_walrus_wrapper_pa_64a3d61c24b24100a10416ee60c44fd7(get_pyarrow())) is not None and isinstance(ser, pa.ChunkedArray)


def is_pyarrow_table(df: Any) -> TypeIs[pa.Table]:
    """Check whether `df` is a PyArrow Table without importing PyArrow.

    Warning:
        This method cannot be called on Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)

    if False:
        pa = NotImplemented

    def _walrus_wrapper_pa_f68d5b7e134b44a180e4df2496826778(expr):
        """Wrapper function for assignment expression."""
        nonlocal pa
        pa = expr
        return pa

    return (_walrus_wrapper_pa_f68d5b7e134b44a180e4df2496826778(get_pyarrow())) is not None and isinstance(df, pa.Table)


def is_pyarrow_scalar(obj: Any) -> TypeIs[pa.Scalar[Any]]:
    if False:
        pa = NotImplemented

    def _walrus_wrapper_pa_f220d9f7c0184085992ff3c18ac1563c(expr):
        """Wrapper function for assignment expression."""
        nonlocal pa
        pa = expr
        return pa

    return (_walrus_wrapper_pa_f220d9f7c0184085992ff3c18ac1563c(get_pyarrow())) is not None and isinstance(obj, pa.Scalar)


def is_pyspark_dataframe(df: Any) -> TypeIs[pyspark_sql.DataFrame]:
    """Check whether `df` is a PySpark DataFrame without importing PySpark.

    Warning:
        This method cannot be called on a Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)

    if False:
        pyspark_sql = NotImplemented

    def _walrus_wrapper_pyspark_sql_62ea7f6548f44ba48380bfd826c59290(expr):
        """Wrapper function for assignment expression."""
        nonlocal pyspark_sql
        pyspark_sql = expr
        return pyspark_sql

    return bool(
        (_walrus_wrapper_pyspark_sql_62ea7f6548f44ba48380bfd826c59290(get_pyspark_sql())) is not None
        and isinstance(df, pyspark_sql.DataFrame)
    )


def is_pyspark_connect_dataframe(df: Any) -> TypeIs[PySparkConnectDataFrame]:
    """Check whether `df` is a PySpark Connect DataFrame without importing PySpark.

    Warning:
        This method cannot be called on a Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)
    if get_pyspark_connect() is not None:  # pragma: no cover
        try:
            from pyspark.sql.connect.dataframe import DataFrame
        except ImportError:
            return False
        return isinstance(df, DataFrame)
    return False


def is_sqlframe_dataframe(df: Any) -> TypeIs[SQLFrameDataFrame]:
    """Check whether `df` is a SQLFrame DataFrame without importing SQLFrame.

    Warning:
        This method cannot be called on a Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)
    if get_sqlframe() is not None:
        from sqlframe.base.dataframe import BaseDataFrame

        return isinstance(df, BaseDataFrame)
    return False  # pragma: no cover


def is_numpy_array(arr: Any | _NDArray[_ShapeT]) -> TypeIs[_NDArray[_ShapeT]]:
    """Check whether `arr` is a NumPy Array without importing NumPy."""

    if False:
        np = NotImplemented

    def _walrus_wrapper_np_5dfdd4ccfe384ea1a53d2acfd25cf9b0(expr):
        """Wrapper function for assignment expression."""
        nonlocal np
        np = expr
        return np

    return (_walrus_wrapper_np_5dfdd4ccfe384ea1a53d2acfd25cf9b0(get_numpy())) is not None and isinstance(arr, np.ndarray)


def is_numpy_array_1d(arr: Any) -> TypeIs[_1DArray]:
    """Check whether `arr` is a 1D NumPy Array without importing NumPy."""
    return is_numpy_array(arr) and arr.ndim == 1


def is_numpy_array_1d_int(arr: Any) -> TypeIs[_1DArrayInt]:
    if False:
        np = NotImplemented

    def _walrus_wrapper_np_216e7edc7440450b8b2279371d2a2477(expr):
        """Wrapper function for assignment expression."""
        nonlocal np
        np = expr
        return np

    return (
        (_walrus_wrapper_np_216e7edc7440450b8b2279371d2a2477(get_numpy()))
        and is_numpy_array_1d(arr)
        and np.issubdtype(arr.dtype, np.integer)
    )


def is_numpy_array_2d(arr: Any) -> TypeIs[_2DArray]:
    """Check whether `arr` is a 2D NumPy Array without importing NumPy."""
    return is_numpy_array(arr) and arr.ndim == 2


def is_numpy_scalar(scalar: Any) -> TypeGuard[_NumpyScalar]:
    """Check whether `scalar` is a NumPy Scalar without importing NumPy."""
    # NOTE: Needs to stay as `TypeGuard`
    # - Used in `Series.__getitem__`, but not annotated
    # - `TypeGuard` is *hiding* that the check introduces an intersection

    if False:
        np = NotImplemented

    def _walrus_wrapper_np_fbd8264d55d64165b444631d57cc453d(expr):
        """Wrapper function for assignment expression."""
        nonlocal np
        np = expr
        return np

    return (_walrus_wrapper_np_fbd8264d55d64165b444631d57cc453d(get_numpy())) is not None and isinstance(scalar, np.generic)


def is_pandas_like_dataframe(df: Any) -> bool:
    """Check whether `df` is a pandas-like DataFrame without doing any imports.

    By "pandas-like", we mean: pandas, Modin, cuDF.

    Warning:
        This method cannot be called on a Narwhals DataFrame/LazyFrame.
    """
    _raise_if_narwhals_df_or_lf(df)
    return is_pandas_dataframe(df) or is_modin_dataframe(df) or is_cudf_dataframe(df)


def is_pandas_like_series(ser: Any) -> bool:
    """Check whether `ser` is a pandas-like Series without doing any imports.

    By "pandas-like", we mean: pandas, Modin, cuDF.

    Warning:
        This method cannot be called on Narwhals Series.
    """
    _raise_if_narwhals_series(ser)
    return is_pandas_series(ser) or is_modin_series(ser) or is_cudf_series(ser)


def is_pandas_like_index(index: Any) -> bool:
    """Check whether `index` is a pandas-like Index without doing any imports.

    By "pandas-like", we mean: pandas, Modin, cuDF.
    """
    return (
        is_pandas_index(index) or is_modin_index(index) or is_cudf_index(index)
    )  # pragma: no cover


def is_into_series(native_series: Any | IntoSeriesT) -> TypeIs[IntoSeriesT]:
    """Check whether `native_series` can be converted to a Narwhals Series.

    Arguments:
        native_series: The object to check.

    Returns:
        `True` if `native_series` can be converted to a Narwhals Series, `False` otherwise.

    Examples:
        >>> import pandas as pd
        >>> import polars as pl
        >>> import numpy as np
        >>> import narwhals as nw

        >>> s_pd = pd.Series([1, 2, 3])
        >>> s_pl = pl.Series([1, 2, 3])
        >>> np_arr = np.array([1, 2, 3])

        >>> nw.dependencies.is_into_series(s_pd)
        True
        >>> nw.dependencies.is_into_series(s_pl)
        True
        >>> nw.dependencies.is_into_series(np_arr)
        False
    """
    from narwhals.series import Series

    return (
        isinstance(native_series, Series)
        or hasattr(native_series, "__narwhals_series__")
        or is_polars_series(native_series)
        or is_pyarrow_chunked_array(native_series)
        or is_pandas_like_series(native_series)
    )


def is_into_dataframe(native_dataframe: Any | IntoDataFrameT) -> TypeIs[IntoDataFrameT]:
    """Check whether `native_dataframe` can be converted to a Narwhals DataFrame.

    Arguments:
        native_dataframe: The object to check.

    Returns:
        `True` if `native_dataframe` can be converted to a Narwhals DataFrame, `False` otherwise.

    Examples:
        >>> import pandas as pd
        >>> import polars as pl
        >>> import numpy as np
        >>> from narwhals.dependencies import is_into_dataframe

        >>> df_pd = pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
        >>> df_pl = pl.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]})
        >>> np_arr = np.array([[1, 4], [2, 5], [3, 6]])

        >>> is_into_dataframe(df_pd)
        True
        >>> is_into_dataframe(df_pl)
        True
        >>> is_into_dataframe(np_arr)
        False
    """
    from narwhals.dataframe import DataFrame

    return (
        isinstance(native_dataframe, DataFrame)
        or hasattr(native_dataframe, "__narwhals_dataframe__")
        or is_polars_dataframe(native_dataframe)
        or is_pyarrow_table(native_dataframe)
        or is_pandas_like_dataframe(native_dataframe)
    )


def is_narwhals_dataframe(
    df: DataFrame[IntoDataFrameT] | Any,
) -> TypeIs[DataFrame[IntoDataFrameT]]:
    """Check whether `df` is a Narwhals DataFrame.

    This is useful if you expect a user to pass in a Narwhals
    DataFrame directly, and you want to catch both `narwhals.DataFrame`
    and `narwhals.stable.v1.DataFrame`.
    """
    from narwhals.dataframe import DataFrame

    return isinstance(df, DataFrame)


def is_narwhals_lazyframe(
    lf: Any | LazyFrame[IntoLazyFrameT],
) -> TypeIs[LazyFrame[IntoLazyFrameT]]:
    """Check whether `lf` is a Narwhals LazyFrame.

    This is useful if you expect a user to pass in a Narwhals
    LazyFrame directly, and you want to catch both `narwhals.LazyFrame`
    and `narwhals.stable.v1.LazyFrame`.
    """
    from narwhals.dataframe import LazyFrame

    return isinstance(lf, LazyFrame)


def is_narwhals_series(ser: Any | Series[IntoSeriesT]) -> TypeIs[Series[IntoSeriesT]]:
    """Check whether `ser` is a Narwhals Series.

    This is useful if you expect a user to pass in a Narwhals
    Series directly, and you want to catch both `narwhals.Series`
    and `narwhals.stable.v1.Series`.
    """
    from narwhals.series import Series

    return isinstance(ser, Series)


def is_narwhals_series_int(ser: Any | Series[IntoSeriesT]) -> TypeIs[Series[IntoSeriesT]]:
    return is_narwhals_series(ser) and ser.dtype.is_integer()


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
