from algs.bubble_sort import parse_txt_file
from algs.comparators import sort_in_ascending, sort_in_descending, sort_ascending_while_tracking
from algs.selection_sort import selection_sort

text = open('../txt_files/sort.txt')


def test_selection_sort_sorts_a_short_list_ascending():
    array = [1, 5, 3, 2, 9, 7, 4]
    result = selection_sort(array, sort_in_ascending)
    assert result == [1, 2, 3, 4, 5, 7, 9]


def test_selection_sort_sorts_a_short_list_descending():
    array = [1, 5, 3, 2, 9, 7, 4]
    result = selection_sort(array, sort_in_descending)
    assert result == [9, 7, 5, 4, 3, 2, 1]


def test_selection_sort_sorts_parsed_text_file_with_odd_event_comparator():
    parsed_text = parse_txt_file(text)
    selection_sort(parsed_text, sort_in_ascending)
    first_ten = parsed_text[:10]
    last_ten = parsed_text[-10:]
    assert first_ten == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert last_ten == [9991, 9992, 9993, 9994, 9995, 9996, 9997, 9998, 9999, 10000]


def test_merge_sort_has_right_number_of_comparisons():
    track = {'comparisons': 0, "copies": 0}
    array = parse_txt_file(text)
    selection_sort(array, sort_ascending_while_tracking, track)
    assert track['comparisons'] == 49995000
    assert track['copies'] == 29964
