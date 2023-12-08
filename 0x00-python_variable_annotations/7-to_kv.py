#!/usr/bin/env python3

"""Typed annotation for string k or fload v"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Function that returns a tuple containing the input string
    and the square of the input int or float.
    """
    return (k, float(v) ** 2)
