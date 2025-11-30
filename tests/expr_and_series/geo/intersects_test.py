from __future__ import annotations

from typing import TYPE_CHECKING, Any, Callable, TypeVar

import geopandas as gpd
import pandas as pd
import pytest

import narwhals as nw
from tests.utils import assert_equal_data

if TYPE_CHECKING:
    import duckdb

T = TypeVar("T", bound=pd.DataFrame | gpd.GeoDataFrame)


def gpd_ser_constructor(data: gpd.GeoSeries) -> gpd.GeoSeries:
    return data


def gpd_constructor(data: gpd.GeoDataFrame | dict[str, pd.Series]) -> gpd.GeoDataFrame:
    # TODO (m-richards) implement as data dict + geo metadata dict
    # TODO (m-richards) making this a GeoDataframe and asserting there is at least one geometry column,
    #   so that we can do gdf['foo'].intersects(gdf['bar'])
    #   because if this were a pd.DataFrame we'd have to do
    #   gdf['foo'].geo.intersects(gdf['bar']) and a GeoSeries doesn't have a .geo namespace
    #   this is probably an api issue in geopandas
    if isinstance(data, dict):
        # assume that dicts are already pandas columns (and therefore already geometry dtype)
        assert all(isinstance(i, pd.Series) for i in data.values())
        out = pd.DataFrame(data)
        geo_cols = out.columns[out.dtypes == "geometry"]
        assert len(geo_cols) > 0, "must have a geometry column"
        return gpd.GeoDataFrame(out).set_geometry(geo_cols[0])

    return data


def duckdb_constructor(data: gpd.GeoDataFrame) -> duckdb.DuckDBPyRelation:
    data = gpd_constructor(data)
    import duckdb

    duckdb.install_extension("spatial")
    duckdb.load_extension("spatial")
    duckdb.sql("CALL register_geoarrow_extensions()")
    # this temp geodataframe might not have an active geometry column
    #  that's okay because it's not something we necessarily want to pass on anyway
    #  perhaps suggests geopandas should have a toplevel function for this?
    _gdf_arrow = gpd.GeoDataFrame(data).to_arrow()
    return duckdb.sql("SELECT * FROM _gdf_arrow")


@pytest.fixture
def test_data_gpd() -> gpd.GeoDataFrame:
    import geopandas as gpd
    from shapely import Point, Polygon

    t1 = Polygon([(0, 0), (1, 0), (1, 1)])
    t2 = Polygon([(0, 0), (1, 1), (0, 1)])
    p0 = Point(5, 5)
    ser = gpd.GeoSeries([t1, t2, p0])
    ser2 = gpd.GeoSeries([t1, t1, t1])
    return gpd.GeoDataFrame({"a": ser, "b": ser2}).set_geometry("a")


@pytest.fixture
def test_data_duckdb(test_data_gpd: gpd.GeoDataFrame) -> None:
    import duckdb

    duckdb.install_extension("spatial")
    duckdb.load_extension("spatial")
    duckdb.sql("CALL register_geoarrow_extensions()")
    _gdf_arrow = test_data_gpd.to_arrow()
    return duckdb.sql("SELECT * FROM _gdf_arrow")


def data_1() -> gpd.GeoSeries:
    # TODO(m-richards) ideally define as dicts
    # (not fixtures to reduce bloat of mandatory type annotations)
    from shapely import Point, Polygon

    t1 = Polygon([(0, 0), (1, 0), (1, 1)])
    t2 = Polygon([(0, 0), (1, 1), (0, 1)])
    p0 = Point(5, 5)
    return gpd.GeoSeries([t1, t2, p0])


def data_2() -> gpd.GeoSeries:
    from shapely import Polygon

    t1 = Polygon([(0, 0), (1, 0), (1, 1)])
    return gpd.GeoSeries([t1, t1, t1])


@pytest.mark.parametrize("geo_ser_constructor", [gpd_ser_constructor])
# TODO(m-richards) fix generic constructor and therefore annotations
def test_intersects_namespace(geo_ser_constructor: Any) -> None:
    ser_native = geo_ser_constructor(data_1())
    nser = nw.from_native(ser_native, series_only=True)
    other_native = geo_ser_constructor(data_2())
    other = nw.from_native(other_native, series_only=True)
    res = nser.geo.intersects(other)
    assert_equal_data({"col": res}, {"col": pd.Series([True, True, False])})


@pytest.mark.parametrize("geo_constructor", [gpd_constructor, duckdb_constructor])
def test_intersects_expr(
    geo_constructor: Callable[
        [pd.DataFrame | gpd.GeoDataFrame | dict[str, pd.Series]], gpd.GeoDataFrame
    ],
) -> None:
    native = geo_constructor({"a": data_1(), "b": data_2()})
    df = nw.from_native(native)

    expr = nw.col("a").geo.intersects(nw.col("b")).alias("c")
    res = df.select(expr)
    assert_equal_data(res, {"c": pd.Series([True, True, False])})
