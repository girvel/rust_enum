# Rust-style enums for Python

Easily-defined enumerations that can contain data and be matched.

Here they are:

```python
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
```

Also Option is implemented, so you can do it even faster in most cases:

```python
def divide(a: float, b: float) -> Option[float]:
    if b == 0: return Option.Nothing()
    return Option.Some(a / b)

assert divide(6, 2).unwrap() == 3
assert divide(6, 2).unwrap_or(None) == 3
assert divide(6, 0).unwrap_or(None) is None
assert divide(6, 2).map(lambda v: v * 3) == Option.Some(9)
assert divide(6, 2).and_then(lambda v: divide(v, 3)) == Option.Some(1)
```

## Installation

```bash
pip install rust_enum
```