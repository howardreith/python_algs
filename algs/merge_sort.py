from math import floor


def merge_sort(array, strategy, track=None):
    if len(array) == 1:
        if (track):
            track['copies'] = track['copies'] + 1
        return array
    middle = floor((len(array) / 2))
    merge_arrays = {'left': [], 'right': []}
    if track:
        merge_arrays['left'] = merge_sort(array[:middle], strategy, track)
        merge_arrays['right'] = merge_sort(array[middle:], strategy, track)
    else:
        merge_arrays['left'] = merge_sort(array[:middle], strategy)
        merge_arrays['right'] = merge_sort(array[middle:], strategy)

    if not len(merge_arrays['left']) or not len(merge_arrays['right']):
        return merge_arrays['left'] or merge_arrays['right']

    result = []
    i, j = 0, 0

    while len(result) < len(merge_arrays['left']) + len(merge_arrays['right']):
        if track:
            comparator_result = strategy(merge_arrays['left'][i], merge_arrays['right'][j], track)
        else:
            comparator_result = strategy(merge_arrays['left'][i], merge_arrays['right'][j])
        if comparator_result < 0:
            result.append(merge_arrays['left'][i])
            if (track):
                track['copies'] = track['copies'] + 1
            i += 1
        else:
            result.append(merge_arrays['right'][j])
            if (track):
                track['copies'] = track['copies'] + 1
            j += 1
        if i == len(merge_arrays['left']) or j == len(merge_arrays['right']):
            result.extend(merge_arrays['left'][i:] or merge_arrays['right'][j:])
            if (track):
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
