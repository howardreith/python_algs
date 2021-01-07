from algs.comparators import sort_in_ascending
from algs.quick_sort import quick_sort, pivot_on_zero


def test_quick_sort_sorts_array_of_numbers_with_zero_pivot():
    array = [1, 5, 3, 2, 9, 7, 4]
    result = quick_sort(array, 7, sort_in_ascending, pivot_on_zero)
    assert result == [1, 2, 3, 4, 5, 7, 9]



# Pivot Strategies

def test_pivot_on_zero_returns_zero():
    result = pivot_on_zero()
    assert result == 0

