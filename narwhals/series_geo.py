from __future__ import annotations

from typing import Any, Generic

from narwhals.typing import SeriesT


class SeriesGeoNamespace(Generic[SeriesT]):
    def __init__(self, series: SeriesT) -> None:
        self._narwhals_series = series

    def intersects(self, other: Any) -> SeriesT:
        return self._narwhals_series._with_compliant(
            self._narwhals_series._compliant_series.geo.intersects(
                self._narwhals_series._extract_native(other)
            )
        )

    def area(self) -> SeriesT:
        return self._narwhals_series._with_compliant(
            self._narwhals_series._compliant_series.geo.area()
        )
