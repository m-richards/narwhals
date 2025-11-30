from __future__ import annotations

from typing import TYPE_CHECKING, Generic, TypeVar

from narwhals._expression_parsing import ExprKind, ExprNode

if TYPE_CHECKING:
    from typing import Any

    from narwhals.expr import Expr

ExprT = TypeVar("ExprT", bound="Expr")


class ExprGeoNamespace(Generic[ExprT]):
    def __init__(self, expr: ExprT) -> None:
        self._expr = expr

    def intersects(self, other: Any) -> ExprT:
        # TODO (m-richards) this form of with binary isn't available generically at the compliant layer?
        return self._expr._with_binary(lambda a, b: a.geo.intersects(b), other)

    def area(self) -> ExprT:
        return self._expr._append_node(ExprNode(ExprKind.ELEMENTWISE, "geo.area"))
