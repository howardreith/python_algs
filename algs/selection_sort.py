def selection_sort(list, strategy, track=None):
    for i in range(len(list) - 1):
        lowest = i

        for j in range(i + 1, len(list)):
            if track:
                result = strategy(list[j], list[lowest], track)
            else:
                result = strategy(list[j], list[lowest])
            if result < 0:
                lowest = j
        list[i], list[lowest] = list[lowest], list[i]
        if track:
            track["copies"] = track["copies"] + 3

    return list
