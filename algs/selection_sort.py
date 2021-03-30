def selection_sort(input_list, strategy, track=None):
    for i in range(len(input_list) - 1):
        lowest = i

        for j in range(i + 1, len(input_list)):
            if track:
                result = strategy(input_list[j], input_list[lowest], track)
            else:
                result = strategy(input_list[j], input_list[lowest])
            if result < 0:
                lowest = j
        if i != lowest:
            input_list[i], input_list[lowest] = input_list[lowest], input_list[i]
            if track:
                track["copies"] = track["copies"] + 3
    return input_list
