import pytest
import random

from abenteuer_informatik.chapter_02_sorting.sorting import quick_sort, select_sort

random.seed(0)


@pytest.fixture
def iterable():
    return random.sample(range(1000), k=100)


def test_select_sort(iterable):
    return sorted(iterable) == select_sort(iterable)


def test_quick_sort(iterable):
    return sorted(iterable) == quick_sort(iterable)
