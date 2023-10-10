import pytest

from rust_enum import enum, Case, Option, UnwrappingError


def test_enum_use_case():
    @enum
    class DivisionResult:
        Undefined = Case()
        Some = Case(number=float)

    def divide(a: float, b: float) -> DivisionResult:
        if b == 0: return DivisionResult.Undefined()
        return DivisionResult.Some(a / b)

    match divide(3, 3):
        case DivisionResult.Some(n): assert n == 1
        case _: assert False


def test_option_use_case():
    def divide(a: float, b: float) -> Option[float]:
        if b == 0: return Option.Nothing()
        return Option.Some(a / b)

    assert divide(6, 2).unwrap() == 3
    assert divide(6, 2).unwrap_or(None) == 3
    assert divide(6, 0).unwrap_or(None) is None
    assert divide(6, 2).map(lambda v: v * 3) == Option.Some(9)
    assert divide(6, 2).and_then(lambda v: divide(v, 3)) == Option.Some(1)
    assert divide(6, 2).some()
    assert not divide(6, 0).some()

    with pytest.raises(UnwrappingError):
        Option.Nothing().unwrap()
