def merge_sort(array, strategy):
    if len(array) == 1:
        return array

    middle = round(len(array) / 2)
    left = merge_sort(array[:middle], strategy)
    right = merge_sort(array[middle:], strategy)

    if not len(left) or not len(right):
        return left or right

    result = []
    i, j = 0, 0

    while len(result) < len(left) + len(right):
        comparator_result = strategy(left[i], right[j])
        if comparator_result < 0:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
        if i == len(left) or j == len(right):
            result.extend(left[i:] or right[j:])
            break
    return result


def parse_text(text):
    lines = text.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].replace('\n', '')
        lines[i] = int(lines[i])
    return lines

