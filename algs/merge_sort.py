from math import floor


def merge_sort(array, strategy, track={'copies': 0, 'comparisons': 0}):
    if len(array) == 1:
        return array
    middle = (len(array) // 2)
    merge_arrays = {'left': [], 'right': []}

    merge_arrays['left'] = merge_sort(array[:middle], strategy, track)
    merge_arrays['right'] = merge_sort(array[middle:], strategy, track)

    if not len(merge_arrays['left']) or not len(merge_arrays['right']):
        return merge_arrays['left'] or merge_arrays['right']

    result = []
    i, j = 0, 0

    while len(result) < len(merge_arrays['left']) + len(merge_arrays['right']):
        comparator_result = strategy(merge_arrays['left'][i], merge_arrays['right'][j], track)
        if comparator_result < 0:
            result.append(merge_arrays['left'][i])
            track['copies'] = track['copies'] + 1
            i += 1
        else:
            result.append(merge_arrays['right'][j])
            track['copies'] = track['copies'] + 1
            j += 1
        if i == len(merge_arrays['left']) or j == len(merge_arrays['right']):
            result.extend(merge_arrays['left'][i:] or merge_arrays['right'][j:])
            if not merge_arrays['left'][i:]:
                track['copies'] = track['copies'] + len(merge_arrays['right'][j:])
            else:
                track['copies'] = track['copies'] + len(merge_arrays['left'][i:])
            break
    return result


def parse_text(path):
    with open(path) as text:
        lines = text.readlines()
        for i in range(len(lines)):
            lines[i] = lines[i].replace('\n', '')
            lines[i] = int(lines[i])
        return lines
