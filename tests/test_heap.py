import pytest

from algs.heap import Heap, default_priority_function
from tests.test_running_median import min_priority_function, max_priority_function


def test_heap_can_be_created_with_proper_parameters():
    result = Heap(5)
    assert result.size == 5
    assert result.items == [None, None, None, None, None]


def test_insert_grows_when_heap_is_full_and_length_is_0():
    heap = Heap(0)
    heap.insert(20)
    assert heap.size == 1
    assert len(heap.items) == 1


def test_insert_grows_when_heap_is_full_and_length_not_0():
    heap = Heap(1)
    assert heap.size == 1
    assert len(heap.items) == 1
    heap.insert(20)
    heap.insert(21)
    assert heap.size == 2
    assert len(heap.items) == 2


def test_insert_adds_value_to_heap():
    heap = Heap(5)
    heap.insert(1)
    heap.insert(3)
    assert heap.items[0] == 3
    assert heap.items[1] == 1


def test_insert_adds_values_to_heap_out_of_order():
    heap = Heap(5)
    heap.insert(1)
    heap.insert(3)
    heap.insert(10)
    heap.insert(6)
    heap.insert(2)
    assert heap.extract() == 10
    assert heap.extract() == 6
    assert heap.extract() == 3
    assert heap.extract() == 2
    assert heap.extract() == 1


def test_extract_returns_value_from_heap():
    heap = Heap(5, default_priority_function)
    heap.insert(1)
    heap.insert(5)
    heap.insert(6)
    result = heap.extract()
    assert result == 6
    result = heap.extract()
    assert result == 5
    result = heap.extract()
    assert result == 1


def test_extract_and_insert_alternating_returns_values():
    heap = Heap(5, default_priority_function)
    heap.insert(1)
    heap.insert(5)
    assert heap.extract() == 5
    heap.insert(6)
    heap.insert(2)
    assert heap.extract() == 6
    heap.insert(6)
    assert heap.extract() == 6
    heap.insert(10)
    heap.insert(1)
    assert heap.get_size() == 4


def test_heap_extract_returns_the_proper_number_when_it_is_the_last():
    min_heap = Heap(10, max_priority_function)

    min_heap.insert(1)
    min_heap.insert(3)
    min_heap.insert(2)
    min_heap.insert(4)
    result = min_heap.extract()
    assert result == 4


def test_heap_behaves_correctly_with_duplicate_values():
    heap = Heap(5, default_priority_function)
    heap.insert(1)
    heap.insert(5)
    heap.insert(3)
    heap.insert(5)
    assert heap.extract() == 5
    assert heap.extract() == 5
    assert heap.extract() == 3
    assert heap.peek() == 1


def test_peek_returns_highest_priority_value():
    heap = Heap(5, default_priority_function)
    heap.insert(1)
    heap.insert(5)
    heap.insert(6)
    heap.insert(2)
    result = heap.peek()
    assert result == 6


def test_get_size_returns_size_of_heap():
    heap = Heap(5, default_priority_function)
    heap.insert(1)
    heap.insert(5)
    heap.insert(6)
    heap.insert(2)
    result = heap.get_size()
    assert result == 4
    heap.extract()
    result = heap.get_size()
    assert result == 3


def test_expand_doubles_the_size_of_the_heap():
    heap = Heap(5)
    heap.insert(1)
    heap.expand()
    assert heap.size == 10
    assert len(heap.items) == 10


def test_delete_raises_exception_if_value_not_present():
    heap = Heap(5)
    heap.insert(1)
    with pytest.raises(Exception):
        heap.delete(4)


def test_delete_removes_target_item_from_heap():
    heap = Heap(5)
    heap.insert(1)
    heap.insert(3)
    heap.insert(2)
    heap.insert(4)
    heap.delete(3)
    assert heap.get_size() == 3
    assert heap.extract() == 4
    assert heap.extract() == 2
