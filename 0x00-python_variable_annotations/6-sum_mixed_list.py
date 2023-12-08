#!/usr/bin/env python3
"""Typed- annotation function for mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    Function that returns the sum of a list.
    """
    return sum(mxd_lst)
