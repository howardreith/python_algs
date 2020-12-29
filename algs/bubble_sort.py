def bubble_sort(array, sorting_strategy, track=None):
    has_swapped = True
    unsorted_to = len(array) - 1
    while has_swapped:
        has_swapped = False
        for i in range(unsorted_to):
            if track:
                result = sorting_strategy(array[i], array[i + 1], track)
            else:
                result = sorting_strategy(array[i], array[i + 1])
            if result > 0:
                array[i], array[i + 1] = array[i + 1], array[i]
                has_swapped = True
        unsorted_to = unsorted_to - 1


def parse_txt_file(text):
    lines = text.readlines()
    for i in range(len(lines)):
        lines[i] = int(lines[i].replace('\n', ''))
    return lines
