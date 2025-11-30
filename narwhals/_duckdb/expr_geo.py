from __future__ import annotations

from typing import TYPE_CHECKING, Any

from narwhals._compliant import LazyExprNamespace
from narwhals._compliant.any_namespace import GeoNamespace
from narwhals._duckdb.utils import F

if TYPE_CHECKING:
    from narwhals._duckdb.expr import DuckDBExpr


class DuckDBExprGeoNamespace(LazyExprNamespace["DuckDBExpr"], GeoNamespace["DuckDBExpr"]):
    def intersects(self, other: Any) -> DuckDBExpr:
        return self._compliant_expr._with_binary(
            lambda expr, other: F("ST_Intersects", expr, other), other
        )

    def area(self) -> DuckDBExpr:
        return self.compliant._with_elementwise(lambda expr: F("ST_Area", expr))
