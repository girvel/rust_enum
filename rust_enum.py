"""Rust-style enumerations."""
from dataclasses import make_dataclass


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
