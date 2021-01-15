from algs.comparators import sort_in_ascending, sort_in_descending, sort_ascending_while_tracking
from algs.merge_sort import parse_text
from algs.quick_sort import quick_sort, pivot_on_zero, pivot_on_random, pivot_on_high, partition

text = '../txt_files/to_merge.txt'


def test_quick_sort_sorts_array_of_numbers_with_zero_pivot():
    array = [1, 5, 3, 2, 9, 7, 4]
    quick_sort(array, 0, 6, sort_in_ascending, pivot_on_zero)
    assert array == [1, 2, 3, 4, 5, 7, 9]


def test_quick_sort_sorts_array_of_numbers_with_random_pivot():
    array = [1, 5, 3, 2, 9, 7, 4]
    quick_sort(array, 0, len(array) - 1, sort_in_ascending, pivot_on_random)
    assert array == [1, 2, 3, 4, 5, 7, 9]


def test_quick_sort_sorts_array_of_numbers_with_high_pivot():
    array = [1, 5, 3, 2, 9, 7, 4]
    quick_sort(array, 0, 6, sort_in_ascending, pivot_on_high)
    assert array == [1, 2, 3, 4, 5, 7, 9]


def test_quick_sort_sorts_array_of_numbers_Descending_with_zero_pivot():
    array = [1, 5, 3, 2, 9, 7, 4]
    quick_sort(array, 0, 6, sort_in_descending, pivot_on_zero)
    assert array == [9, 7, 5, 4, 3, 2, 1]


def test_quick_sort_sorts_array_of_numbers_Descending_with_random_pivot():
    array = [1, 5, 3, 2, 9, 7, 4]
    quick_sort(array, 0, 6, sort_in_descending, pivot_on_random)
    assert array == [9, 7, 5, 4, 3, 2, 1]


def test_quick_sort_sorts_array_of_numbers_Descending_with_random_pivot():
    array = [1, 5, 3, 2, 9, 7, 4]
    quick_sort(array, 0, 6, sort_in_descending, pivot_on_high)
    assert array == [9, 7, 5, 4, 3, 2, 1]


def test_quick_sort_sorts_the_challenge_list():
    array = parse_text(text)
    quick_sort(array, 0, len(array) - 1, sort_in_ascending, pivot_on_zero)
    assert array[:20] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert array[-20:] == [9981, 9982, 9983, 9984, 9985, 9986, 9987, 9988, 9989, 9990, 9991, 9992, 9993, 9994, 9995,
                           9996, 9997, 9998, 9999, 10000]


def test_quick_sort_has_right_number_of_comparisons():
    track = {'comparisons': 0, 'copies': 0}
    array = parse_text(text)
    quick_sort(array, 0, len(array) - 1, sort_ascending_while_tracking, pivot_on_zero, track)
    assert track['comparisons'] == 171705
    assert track['copies'] == 113769


def test_partition_returns_proper_high():
    array = [8, 9, 2, 1, 4, 10, 5]
    result = partition(array, 0, len(array) - 1, sort_in_ascending)
    assert result == 4


# Pivot Strategies

def test_pivot_on_zero_returns_zero():
    result = pivot_on_zero(0, 0)
    assert result == 0


def test_pivot_on_random_returns_random_number_between_range():
    result = pivot_on_random(0, 10)
    assert result >= 0
    assert result < 10


def test_pivot_on_high_returns_high_number():
    result = pivot_on_high(0, 7)
    assert result == 6
