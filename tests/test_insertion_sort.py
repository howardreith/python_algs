import random

from algs.bubble_sort import parse_txt_file
from algs.comparators import sort_in_ascending, sort_in_descending, sort_ascending_while_tracking
from algs.insertion_sort import insertion_sort_wrong, parse_text, update_score_tracker, print_top_ten, insertion_sort

text = open('../txt_files/super_sport.txt')
lotsa_numbers = open('../txt_files/to_merge.txt')

def test_insertion_sort_sorts_a_short_list_of_numbers():
    array = [5, 3, 7]
    result = insertion_sort_wrong(array, sort_in_ascending)
    assert result == [3, 5, 7]


def test_insertion_correct_sort_sorts_a_short_list_of_numbers():
    array = [5, 3, 7]
    result = insertion_sort(array, sort_in_ascending)
    assert result == [3, 5, 7]


def test_insertion_sort_sorts_a_list_of_numbers():
    array = [5, 6, 4, 3, 8, 7]
    result = insertion_sort_wrong(array, sort_in_ascending)
    assert result == [3, 4, 5, 6, 7, 8]


def test_insertion_sort_correct_sorts_a_list_of_numbers():
    array = [5, 6, 4, 3, 8, 7]
    result = insertion_sort(array, sort_in_ascending)
    assert result == [3, 4, 5, 6, 7, 8]


def test_insertion_sort_sorts_a_random_list_of_numbers():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(array)
    result = insertion_sort_wrong(array, sort_in_ascending)
    assert result == expected


def test_insertion_sort_correct_sorts_a_random_list_of_numbers():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(array)
    result = insertion_sort(array, sort_in_ascending)
    assert result == expected


def test_insertion_sort_sorts_array_of_strings():
    array = ["cat", "dog", "bird", "fish", "snake"]
    result = insertion_sort_wrong(array, sort_in_ascending)
    assert result == ["bird", "cat", "dog", "fish", "snake"]


def test_insertion_sort_correct_sorts_array_of_strings():
    array = ["cat", "dog", "bird", "fish", "snake"]
    result = insertion_sort(array, sort_in_ascending)
    assert result == ["bird", "cat", "dog", "fish", "snake"]


def test_insertion_sort_sorts_a_random_list_of_strings():
    array = ["bird", "cat", "dog", "fish", "octopus", "snake"]
    expected = ["bird", "cat", "dog", "fish", "octopus", "snake"]
    random.shuffle(array)
    result = insertion_sort_wrong(array, sort_in_ascending)
    assert result == expected


def test_insertion_sort_correct_sorts_a_random_list_of_strings():
    array = ["bird", "cat", "dog", "fish", "octopus", "snake"]
    expected = ["bird", "cat", "dog", "fish", "octopus", "snake"]
    random.shuffle(array)
    result = insertion_sort(array, sort_in_ascending)
    assert result == expected


def test_insertion_sort_sorts_a_list_of_numbers_descending():
    array = [5, 6, 4, 3, 8, 7]
    result = insertion_sort_wrong(array, sort_in_descending)
    assert result == [8, 7, 6, 5, 4, 3]


def test_insertion_sort_correct_sorts_a_list_of_numbers_descending():
    array = [5, 6, 4, 3, 8, 7]
    result = insertion_sort(array, sort_in_descending)
    assert result == [8, 7, 6, 5, 4, 3]


def test_parse_text_parses_text():
    result = parse_text(text)
    assert len(result) == 100
    assert result[0]['name'] == 'Owen Slater'
    assert result[0]['score'] == '8.401877'


def test_update_score_tracker_returns_a_sorted_score_tracker():
    score_tracker = []
    results = parse_text(text)
    update_score_tracker(score_tracker, results)
    assert len(score_tracker) == 100
    assert score_tracker[0]['name'] == 'Brandon Powell'
    assert score_tracker[0]['score'] == '0.163006'


def test_print_top_10_prints_the_top_10_with_text_file():
    score_tracker = []
    results = parse_text(text)
    update_score_tracker(score_tracker, results)
    print_top_ten(score_tracker)


def test_insertion_sort_has_right_number_of_comparisons():
    track = {'comparisons': 0, "copies": 0}
    array = parse_txt_file(lotsa_numbers)
    insertion_sort(array, sort_ascending_while_tracking, track)
    assert track['comparisons'] == 23958117
    assert track['copies'] == 23968128
