# -*- coding: utf-8 -*-
# Copyright (c) CDU

"""Model Docstrings

"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from collections import deque
from operator import pos, neg
from typing import Union, Sequence

try:
    from typing import Self
except ImportError:
    from typing_extensions import Self

_lite_mode = object()


class Average(object):
    """
    Average

    Represents the average of a series
    """

    def __init__(self, count: int = None, total: Union[int, float] = None, seq: Sequence = None):
        """

        :param count:
        :param total:
        :param seq:
        :param lite:
        """
        self._count: int = count or 0
        self._total: Union[int, float] = total or 0
        if seq:
            self._seq: deque = deque(seq)
        else:
            self._seq: object = _lite_mode

    @property
    def count(self) -> int:
        return self._count

    @property
    def total(self) -> Union[int, float]:
        return self._total

    @property
    def seq(self) -> Union[None, deque]:
        if self._seq == _lite_mode or self._seq is None:
            return None
        else:
            self._seq: deque
            return self._seq.copy()

    def __len__(self) -> int:
        return self._count

    def __getitem__(self, item):
        if self._seq == _lite_mode:
            raise TypeError("lite Average not support average[key] call.")
        else:
            self._seq: deque
            return self._seq[item]

    def __setitem__(self, key, value):
        if self._seq == _lite_mode:
            raise TypeError("lite Average not support average[key] = value.")
        else:
            self._seq: deque
            return self._seq[key] == value

    def __delitem__(self, key):
        if self._seq == _lite_mode:
            raise TypeError("lite Average not support del average[key].")
        else:
            self._seq: deque
            del self._seq[key]

    def __lt__(self, other):
        """Return Average() < other"""
        if isinstance(other, type(self)):
            return float(self) < float(other)
        elif isinstance(other, (int, float)):
            return float(self) < other
        else:
            raise TypeError("Only support int, float and Average")

    def __le__(self, other):
        """Return Average() <= other"""
        if isinstance(other, type(self)):
            return float(self) <= float(other)
        elif isinstance(other, (int, float)):
            return float(self) <= other
        else:
            raise TypeError("Only support int, float and Average")

    def __eq__(self, other):
        """Return Average() == other"""
        if isinstance(other, type(self)):
            return float(self) == float(other)
        elif isinstance(other, (int, float)):
            return float(self) == other
        else:
            raise TypeError("Only support int, float and Average")

    def __ne__(self, other):
        """Return Average() != other"""
        if isinstance(other, type(self)):
            return float(self) != float(other)
        elif isinstance(other, (int, float)):
            return float(self) != other
        else:
            raise TypeError("Only support int, float and Average")

    def __gt__(self, other):
        """Return Average() > other"""
        if isinstance(other, type(self)):
            return float(self) > float(other)
        elif isinstance(other, (int, float)):
            return float(self) > other
        else:
            raise TypeError("Only support int, float and Average")

    def __ge__(self, other):
        """Return Average() >= other"""
        if isinstance(other, type(self)):
            return float(self) >= float(other)
        elif isinstance(other, (int, float)):
            return float(self) >= other
        else:
            raise TypeError("Only support int, float and Average")

    def __add__(self, other: Union[int, float, Self]):
        count, total = self._count, self._total
        if isinstance(other, type(self)):
            count += other.count
            total += other.total
        else:
            count += 1
            total += other
        if isinstance(other, type(self)) and self.seq and other.seq:
            seq = self.seq
            seq.extend(other.seq)
        else:
            seq = None
        return type(self)(count, total, seq)

    def __iadd__(self, other):
        if isinstance(other, type(self)):
            self._count += other.count
            self._total += other.total
        else:
            self._count += 1
            self._total += other
        if isinstance(other, type(self)) and self.seq and other.seq:
            self._seq.extend(other.seq)
        else:
            self._seq = None
        return self

    def __sub__(self, other: Union[int, float, Self]):
        count, total = self._count, self._total
        if isinstance(other, type(self)):
            count -= other.count
            total -= other.total
        else:
            count -= 1
            total -= other
        if isinstance(other, type(self)) and self.seq and other.seq:
            seq = self.seq
            seq.extend(other.seq)
        else:
            seq = None
        return type(self)(count, total, seq)

    def __isub__(self, other):
        if isinstance(other, type(self)):
            self._count -= other.count
            self._total -= other.total
        else:
            self._count -= 1
            self._total -= other
        if isinstance(other, type(self)) and self.seq and other.seq:
            self._seq.extend(other.seq)
        else:
            self._seq = None
        return self

    def __pos__(self):
        return pos(self._total / self._count)

    def __neg__(self):
        return neg(self._total / self._count)

    def __abs__(self):
        return abs(self._total / self._count)

    def __int__(self):
        return int(self._total / self._count)

    def __float__(self):
        return self._total / self._count

    def __round__(self, n=None):
        return round(float(self), n)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return False

    def __repr__(self):
        return f"<Average: {self._total}/{self._count} {float(self):.7f}>"
