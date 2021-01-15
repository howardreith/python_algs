import random


def quick_sort(array, start, end, sort_strategy, pivot_strategy, track={'copies': 0, 'comparisons': 0}):
    if start < end:
        pivot_point = pivot_strategy(start, end)
        array[start], array[pivot_point] = array[pivot_point], array[start]
        track['copies'] = track['copies'] + 3

        pivot = partition(array, start, end, sort_strategy, track)
        quick_sort(array, start, pivot - 1, sort_strategy, pivot_strategy, track)
        quick_sort(array, pivot + 1, end, sort_strategy, pivot_strategy, track)


def partition(array, start, end, sort_strategy, track={'copies': 0, 'comparisons': 0}):
    low = start + 1
    high = end
    pivot_value = array[start]
    while True:
        while low < high and sort_strategy(array[low], pivot_value, track) < 0:
            low += 1
        while high >= low and sort_strategy(array[high], pivot_value, track) >= 0:
            high -= 1

        if low >= high:
            break

        array[low], array[high] = array[high], array[low]
        low += 1
        high -= 1
        track['copies'] = track['copies'] + 3

    array[high], array[start] = array[start], array[high]
    track['copies'] = track['copies'] + 3
    return high


# Pivot Strategies

def pivot_on_zero(start, end):
    return start


def pivot_on_random(start, end):
    return random.randint(start, end)


def pivot_on_high(start, end):
    return end - 1
