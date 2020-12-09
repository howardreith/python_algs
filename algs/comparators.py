def sort_in_ascending(a, b):
    if a > b:
        return 1
    elif b > a:
        return -1
    else:
        return 0


def sort_in_descending(a, b):
    if a < b:
        return 1
    elif b < a:
        return -1
    else:
        return 0