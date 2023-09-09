from rust_enum import enum, Case


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
