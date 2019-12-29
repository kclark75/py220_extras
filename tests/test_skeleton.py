# -*- coding: utf-8 -*-

import pytest
from uw_py220_extras.skeleton import fib

__author__ = "Andy Miles"
__copyright__ = "Andy Miles"
__license__ = "mit"


def test_fib():
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(7) == 13
    with pytest.raises(AssertionError):
        fib(-10)
