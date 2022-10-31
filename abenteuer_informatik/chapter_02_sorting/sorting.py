from typing import Iterable, List


def select_sort(iterable: Iterable) -> List:
    iterable = list(iterable)
    result = []
    while iterable:
        i_min, _ = min(enumerate(iterable), key=lambda x: x[1])
        result.append(iterable.pop(i_min))

    return result


def quick_sort(iterable: Iterable) -> List:
    iterable = list(iterable)
    if len(iterable) <= 1:
        return iterable

    pivot_element = iterable.pop()
    smaller_elements = [x for x in iterable if x <= pivot_element]
    greater_elements = [x for x in iterable if x > pivot_element]
    return [*quick_sort(smaller_elements), pivot_element, *quick_sort(greater_elements)]
