import pytest

from algs.heap import Heap


def test_heap_can_be_created_with_proper_parameters():
    def priority_function(item1, item2):
        return item1 - item2

    result = Heap(5, priority_function)
    assert result.size == 5
    assert result.items == [None, None, None, None, None, None]


def test_insert_raises_exception_when_heap_is_full():
    def priority_function(item1, item2):
        return item1 - item2

    heap = Heap(0, priority_function)
    with pytest.raises(Exception):
        heap.insert(20)


def test_insert_adds_value_to_heap():
    def priority_function(item1, item2):
        return item1 - item2

    heap = Heap(5, priority_function)
    heap.insert(1)
    heap.insert(3)
    assert heap.items[0] == 3
    assert heap.items[1] == 1


def test_extract_returns_value_from_heap():
    def priority_function(item1, item2):
        return item1 - item2
    heap = Heap(5, priority_function)
    heap.insert(1)
    heap.insert(5)
    heap.insert(6)
    result = heap.extract()
    # assert result == 5
    print(heap.items)
    # assert heap.items[0] == 1
    # assert heap.items[1] is None

# insert things that are out of priority order and test the result
# assert the right values on each extract
# switch off between inserts and extracts in some tests
# Test duplicate priorities (insert(1)) (insert(1)) etc.
# Write a test with a bubble down with a full queue. This should move the item
# at the end