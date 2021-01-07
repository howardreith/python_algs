def quick_sort(array, num_items, sort_strategy, pivot_strategy):
    if num_items <= 1:
        return

    pivot = pivot_strategy(num_items)
    store = array[0]
    array[0] = array[pivot]
    array[pivot] = store
    pivot = partition(array, pivot)

    quick_sort(array[0], pivot, sort_strategy, pivot_strategy)
    pivot = pivot + 1
    quick_sort(array[pivot], (num_items - pivot), sort_strategy, pivot_strategy)


def partition(array, num_items):
    low = 1
    high = num_items - 1

    while True:
        while low < high and array[low] < array[0]:
            low = low + 1

        while high >= low and array[high] >= array[0]:
            high = low - 1

        if low >= high:
            break

    store = array[0]
    array[0] = array[high]
    array[high] = store
    return high
# Pivot Strategies

def pivot_on_zero(num_items):
    return 0


def pivot_on_random():
    return


def swap(a, b):
    return

