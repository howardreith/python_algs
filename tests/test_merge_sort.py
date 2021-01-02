from algs.comparators import sort_in_ascending, sort_in_descending, sort_ascending_while_tracking
from algs.merge_sort import merge_sort, parse_text

text = open('../txt_files/to_merge.txt')


def test_merge_sort_returns_array_of_1():
    array = [5]
    result = merge_sort(array, sort_in_ascending)
    assert result == array


def test_merge_sort_sorts_a_short_list_ascending():
    array = [1, 5, 3, 2, 9, 7, 4]
    result = merge_sort(array, sort_in_ascending)
    assert result == [1, 2, 3, 4, 5, 7, 9]


def test_merge_sort_sorts_a_short_list_descending():
    array = [1, 5, 3, 2, 9, 7, 4]
    result = merge_sort(array, sort_in_descending)
    assert result == [9, 7, 5, 4, 3, 2, 1]


def test_merge_sort_sorts_a_short_list_of_strings_ascending():
    array = ['lizard', 'cat', 'snake', 'dog']
    result = merge_sort(array, sort_in_ascending)
    assert result == ['cat', 'dog', 'lizard', 'snake']


def test_merge_sort_sorts_a_short_list_of_strings_descending():
    array = ['lizard', 'cat', 'snake', 'dog']
    result = merge_sort(array, sort_in_descending)
    assert result == ['snake', 'lizard', 'dog', 'cat']


def test_merge_sort_performs_one_operation_for_2_item_unsorted_list():
    track = {'comparisons': 0}
    array = [2, 1]
    merge_sort(array, sort_ascending_while_tracking, track)
    assert track['comparisons'] == 1


def test_merge_sort_performs_two_operation_for_2_item_unsorted_list():
    track = {'comparisons': 0}
    array = [2, 4, 1]
    merge_sort(array, sort_ascending_while_tracking, track)
    assert track['comparisons'] == 2


def test_merge_sort_performs_many_operation_for_complex_unsorted_list():
    track = {'comparisons': 0}
    array = [6, 3, 9, 4, 1, 10, 11, 7, 2, 8]
    merge_sort(array, sort_ascending_while_tracking, track)
    assert track['comparisons'] == 22


def test_parse_text_parses_text():
    array = parse_text(text)
    assert array[:10] == [2148, 9058, 7742, 3153, 6324, 609, 7628, 5469, 7017, 504]


def test_merge_sort_sorts_the_challenge_list():
    array = parse_text(text)
    result = merge_sort(array, sort_in_ascending)
    assert result[:20] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert result[-20:] == [9981, 9982, 9983, 9984, 9985, 9986, 9987, 9988, 9989, 9990, 9991, 9992, 9993, 9994, 9995,
                            9996, 9997, 9998, 9999, 10000]


def test_merge_sort_has_right_number_of_comparisons():
    track = {'comparisons': 0, 'copies': 0}
    array = parse_text(text)
    result = merge_sort(array, sort_ascending_while_tracking, track)
    assert result[:20] == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    assert result[-20:] == [9981, 9982, 9983, 9984, 9985, 9986, 9987, 9988, 9989, 9990, 9991, 9992, 9993, 9994, 9995,
                            9996, 9997, 9998, 9999, 10000]
    assert track['comparisons'] == 120473
    assert track['copies'] == 140472
