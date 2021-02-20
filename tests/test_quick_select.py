from algs.comparators import sort_in_ascending, sort_in_descending
from algs.merge_sort import parse_text
from algs.quick_sort import pivot_on_zero
from algs.quick_select import quick_select

text = '../txt_files/sort.txt'


def test_quick_select_finds_lowest_number_in_list():
    array = [1, 5, 3, 2, 9, 7, 4]
    result = quick_select(array, 0, len(array) - 1, 0, sort_in_ascending)
    assert result == 1


def test_quick_select_finds_second_number_in_list():
    array = [1, 5, 3, 2, 9, 7, 4]
    result = quick_select(array, 0, len(array) - 1, 1, sort_in_ascending)
    assert result == 2


def test_quick_select_finds_third_number_in_list():
    array = [1, 5, 3, 2, 9, 7, 4]
    result = quick_select(array, 0, len(array) - 1, 2, sort_in_ascending)
    assert result == 3


def test_quick_select_finds_fourth_number_in_list():
    array = [1, 5, 3, 2, 9, 7, 4]
    result = quick_select(array, 0, len(array) - 1, 3, sort_in_ascending)
    assert result == 4


def test_quick_select_finds_fifth_number_in_list():
    array = [1, 5, 3, 2, 9, 7, 4]
    result = quick_select(array, 0, len(array) - 1, 4, sort_in_ascending)
    assert result == 5


def test_quick_select_finds_sixth_number_in_list():
    array = [1, 5, 3, 2, 9, 7, 4]
    result = quick_select(array, 0, len(array) - 1, 5, sort_in_ascending)
    assert result == 7


def test_quick_select_finds_highest_number_in_list():
    array = [1, 5, 3, 2, 9, 7, 4]
    result = quick_select(array, 0, len(array) - 1, 6, sort_in_ascending)
    assert result == 9


def test_quick_select_gets_median_of_text():
    array = parse_text(text)
    result = quick_select(array, 0, len(array) - 1, len(array) / 2, sort_in_ascending)
    assert result == 5001
