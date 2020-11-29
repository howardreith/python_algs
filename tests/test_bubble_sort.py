import random

from algs.bubble_sort import bubble_sort, parse_txt_file

text = open('../txt_files/sort.txt')


def comparator(a, b):
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0


def odd_even_comparator(a, b):
    a_is_even = a % 2 == 0
    b_is_even = b % 2 == 0

    if a_is_even is True and b_is_even is False:
        return 1
    if a_is_even is False and b_is_even is True:
        return -1

    return a - b


def test_bubble_sort_sorts_array_of_numbers():
    array = [1, 5, 3, 2, 7]
    bubble_sort(array, comparator)
    assert array == [1, 2, 3, 5, 7]


def test_bubble_sort_sorts_a_random_list_of_numbers():
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    random.shuffle(array)
    bubble_sort(array, comparator)
    assert array == expected


def test_bubble_sort_sorts_array_of_strings():
    array = ["cat", "dog", "bird", "fish", "snake"]
    bubble_sort(array, comparator)
    assert array == ["bird", "cat", "dog", "fish", "snake"]


def test_bubble_sort_sorts_a_random_list_of_strings():
    array = ["bird", "cat", "dog", "fish", "octopus", "snake"]
    expected = ["bird", "cat", "dog", "fish", "octopus", "snake"]
    random.shuffle(array)
    bubble_sort(array, comparator)
    assert array == expected


def test_bubble_sort_sorts_with_odds_ascending_evens_descending():
    array = [3, 4, 8, 6, 9, 1]
    expected = [1, 3, 9, 4, 6, 8]
    bubble_sort(array, odd_even_comparator)
    assert array == expected


def test_bubble_sort_sorts_parsed_text_file_with_odd_event_comparator():
    parsed_text = parse_txt_file(text)
    print(parsed_text)
    bubble_sort(parsed_text, odd_even_comparator)
    first_ten = parsed_text[:10]
    last_ten = parsed_text[-10:]
    assert first_ten == [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    assert last_ten == [9982, 9984, 9986, 9988, 9990, 9992, 9994, 9996, 9998, 10000]