import random


from algs.comparators import sort_in_descending
from algs.quick_sort import quick_sort, pivot_on_zero


def quick_select(array, left, right, desired, sort_strategy):
    if right == left:
        return array[right]

    rand = random.randint(left, right)
    array[left], array[rand] = array[rand], array[left]
    pivot = partition(array, left, right, sort_strategy)

    if pivot == desired:
        return array[pivot]

    if pivot > desired:
        return quick_select(array, left, pivot - 1, desired, sort_strategy)

    return quick_select(array, pivot + 1, right, desired, sort_strategy)


def partition(array, start, end, sort_strategy):
    low = start + 1
    high = end
    pivot_value = array[start]
    while True:
        while low < high and sort_strategy(array[low], pivot_value) < 0:
            low += 1
        while high >= low and sort_strategy(array[high], pivot_value) >= 0:
            high -= 1

        if low >= high:
            break

        array[low], array[high] = array[high], array[low]
        low += 1
        high -= 1

    array[high], array[start] = array[start], array[high]
    return high
