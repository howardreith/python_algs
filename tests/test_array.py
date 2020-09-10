import pytest

from algs.array import Array


def test_array_can_be_created_with_proper_parameters():
    result = Array(10)
    assert result.get_size() == 10
    assert result.get_array_items() == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_raises_exception_with_invalid_insert_index():
    array = Array(10)
    with pytest.raises(Exception):
        array.insert(20, 20)


def test_insert_adds_to_array_at_proper_index():
    array = Array(10)
    array.insert(4, 23)
    assert array.get_array_items()[4] == 23


def test_raises_exception_with_invalid_delete_index():
    array = Array(10)
    with pytest.raises(Exception):
        array.delete(20)


def test_deletes_value_from_array():
    array = Array(10)
    array.insert(1, 5)
    array.insert(2, 6)
    array.insert(3, 7)
    array.delete(2)
    assert array.get_array_items()[1] == 5
    assert array.get_array_items()[2] == 7
    assert array.get_array_items()[3] == 0


def test_search_returns_value_when_present():
    array = Array(10)
    result = array.search(5)
    assert result == -1


def test_search_returns_negative_one_when_not_found():
    array = Array(10)
    array.insert(1, 5)
    result = array.search(5)
    assert result == 1
