from algs.heap import Heap
from algs.running_median import RunningMedian
text = '../txt_files/random_floating_points.txt'

def max_priority_function(item1, item2):
    return item1 - item2


def min_priority_function(item1, item2):
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
    # assert sum == 4995738.755804
    assert sum == 4995738.755804099