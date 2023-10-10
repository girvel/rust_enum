"""Rust-style enumerations."""
from collections.abc import Generator
from dataclasses import make_dataclass
from typing import Any, TypeVar, Generic, Callable


def enum(cls):
    """Create enumeration from class."""
    for field_name in dir(cls):
        if not isinstance((value := getattr(cls, field_name)), Case): continue
        setattr(cls, field_name, make_dataclass(field_name, list(value.dict.items()), bases=(cls, )))
    return cls


class Case:
    """Class-placeholder for generation of enumeration members."""
    def __init__(self, **attributes):
        self.dict = attributes

    # to disable warnings
    def __call__(self, *args, **kwargs):
        pass


class UnwrappingError(Exception): pass

T = TypeVar("T")

@enum
class Option(Generic[T]):
    Some = Case(value=T)
    Nothing = Case()

    def unwrap(self) -> T:
        match self:
            case Option.Some(value): return value
            case _: raise UnwrappingError

    D = TypeVar("D")

    def unwrap_or(self, default_value: D = None) -> T | D:
        match self:
            case Option.Some(value): return value
            case _: return default_value

    R = TypeVar("R")

    def map(self, mapping_function: Callable[[T], R]) -> "Option[R]":
        match self:
            case Option.Some(value): return Option.Some(mapping_function(value))
            case _: return self

    def and_then(self, mapping_function: Callable[[T], R]) -> "Option.Nothing | R":
        match self:
            case Option.Some(value): return mapping_function(value)
            case _: return self

    def some(self):
        match self:
            case Option.Some(_): return True
            case _: return False

    @classmethod
    def next(cls, generator: Generator) -> "Option[Any]":
        return next((cls.Some(e) for e in generator), cls.Nothing())