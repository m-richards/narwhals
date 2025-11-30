from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from typing import Any

    from narwhals.expr import Expr

ExprT = TypeVar("ExprT", bound="Expr")


class ExprGeoNamespace(Generic[ExprT]):
    def __init__(self, expr: ExprT) -> None:
        self._expr = expr

    def intersects(self, other: Any) -> ExprT:
        return self._expr._with_binary(lambda a, b: a.geo.intersects(b), other)
