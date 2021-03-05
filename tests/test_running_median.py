import pytest

from algs.heap import Heap
from algs.running_median import RunningMedian

text = '../txt_files/random_floating_points.txt'


def max_priority_function(item1, item2):
    if item1 is None or item2 is None:
        return item1 or item2
    return item1 - item2


def min_priority_function(item1, item2):
    if item1 is None or item2 is None:
        return item1 or item2
    return item2 - item1


def test_running_median_finds_running_median_with_heaps_set_up():
    min_heap = Heap(10, max_priority_function)
    min_heap.insert(3)
    min_heap.insert(5)
    max_heap = Heap(10, min_priority_function)
    max_heap.insert(7)
    max_heap.insert(9)
    new_value = 4
    sut = RunningMedian()
    result = sut.running_median(min_heap, max_heap, new_value)
    assert result == 5
    result = sut.running_median(min_heap, max_heap, 6)
    assert result == 5.5
    result = sut.running_median(min_heap, max_heap, 10)
    assert result == 6


def test_running_median_finds_running_median_along_way():
    min_heap = Heap(10, max_priority_function)
    max_heap = Heap(10, min_priority_function)
    new_value = 4
    sut = RunningMedian()
    result = sut.running_median(min_heap, max_heap, new_value)
    assert result == 4
    result = sut.running_median(min_heap, max_heap, 6)
    assert result == 5
    result = sut.running_median(min_heap, max_heap, 10)
    assert result == 6


def test_balance_heaps_balanced_an_imbalanced_pair_of_heaps():
    min_heap = Heap(10, max_priority_function)
    max_heap = Heap(10, min_priority_function)

    min_heap.insert(1)
    min_heap.insert(3)
    min_heap.insert(2)
    min_heap.insert(4)
    max_heap.insert(7)
    max_heap.insert(5)

    sut = RunningMedian()
    sut.balance_heaps(min_heap, max_heap)
    assert min_heap.get_size() == 3
    assert max_heap.get_size() == 3
    assert 4 in max_heap.items
    assert 4 not in min_heap.items


def test_is_balanced_returns_true_with_balanced_heaps():
    min_heap = Heap(5, max_priority_function)
    max_heap = Heap(5, min_priority_function)

    min_heap.insert(1)
    min_heap.insert(3)
    min_heap.insert(2)
    max_heap.insert(6)
    max_heap.insert(7)
    max_heap.insert(5)

    sut = RunningMedian()
    result = sut.is_balanced(min_heap, max_heap)
    assert result is True


def test_is_balanced_returns_true_when_heaps_odd_and_off_by_one():
    min_heap = Heap(5, max_priority_function)
    max_heap = Heap(5, min_priority_function)

    min_heap.insert(1)
    min_heap.insert(3)
    min_heap.insert(2)
    max_heap.insert(6)
    max_heap.insert(7)

    sut = RunningMedian()
    result = sut.is_balanced(min_heap, max_heap)
    assert result is True


def test_is_balanced_returns_false_when_heaps_off_by_more_than_one():
    min_heap = Heap(5, max_priority_function)
    max_heap = Heap(5, min_priority_function)

    min_heap.insert(1)
    min_heap.insert(3)
    min_heap.insert(2)
    max_heap.insert(6)

    sut = RunningMedian()
    result = sut.is_balanced(min_heap, max_heap)
    assert result is False


def test_parse_text_file_parses_text():
    sut = RunningMedian()
    result = sut.parse_text_file(text)
    assert len(result) == 100000
    assert result[0] == float(0)
    assert result[1] == float(0.098539)
    assert result[-1] == float(43.629076)
    assert result[55052] == float(32.755712)


def test_running_median_challenge():
    sut = RunningMedian()
    array = sut.parse_text_file(text)
    min_heap = Heap(10, max_priority_function)
    max_heap = Heap(10, min_priority_function)
    sum = 0
    for float_number in array:
        sum += sut.running_median(min_heap, max_heap, float_number)
    assert sum == pytest.approx(4995738.755804, .000001)


def test_maintain_sliding_window_reduces_size_appropriately():
    sut = RunningMedian()
    array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    min_heap = Heap(10, max_priority_function)
    max_heap = Heap(10, min_priority_function)
    for i in range(5):
        min_heap.insert(array[i])
        max_heap.insert(array[i + 5])
    sut.maintain_sliding_window(min_heap, max_heap, array, 11, 10)
    assert array[0] == 2
    assert len(array) == 10
    assert array[-1] != 10


def test_running_media_with_sliding_window_behaves_appropriately_with_challenge():
    sut = RunningMedian()
    array = sut.parse_text_file(text)
    min_heap = Heap(10, max_priority_function)
    max_heap = Heap(10, min_priority_function)
    sum = 0
    window = []
    for float_number in array:
        sum += sut.running_median_with_sliding_window(min_heap, max_heap, float_number, window, 100)
    expected_result = 4995205.397700
    assert sum == pytest.approx(expected_result, 0.0001)


def test_running_media_with_sliding_window_works_with_individual_additions():
    min_heap = Heap(10, max_priority_function)
    max_heap = Heap(10, min_priority_function)
    window = []
    new_value = 4
    sut = RunningMedian()
    result = sut.running_median_with_sliding_window(min_heap, max_heap, new_value, window, 3)
    assert result == 4
    result = sut.running_median_with_sliding_window(min_heap, max_heap, 6, window, 3)
    assert result == 5
    result = sut.running_median_with_sliding_window(min_heap, max_heap, 10, window, 3)
    assert result == 6
    result = sut.running_median_with_sliding_window(min_heap, max_heap, 1, window, 3)
    assert result == 6
    result = sut.running_median_with_sliding_window(min_heap, max_heap, 11, window, 3)
    assert result == 10
    result = sut.running_median_with_sliding_window(min_heap, max_heap, 2, window, 3)
    assert result == 2
