from __future__ import annotations

from typing import TYPE_CHECKING

from narwhals._compliant.any_namespace import GeoNamespace
from narwhals._pandas_like.utils import PandasLikeSeriesNamespace

if TYPE_CHECKING:
    from narwhals._pandas_like.series import PandasLikeSeries


class PandasLikeSeriesGeoNamespace(
    PandasLikeSeriesNamespace, GeoNamespace["PandasLikeSeries"]
):
    def intersects(self, other: PandasLikeSeries) -> PandasLikeSeries:
        return self.with_native(self.native.intersects(other.native))
