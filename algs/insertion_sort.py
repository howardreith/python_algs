from algs.comparators import sort_in_ascending


def insertion_sort(array, sorting_strategy, track=None):
    for i in range(1, len(array)):
        current = array[i]
        if track:
            track['copies'] = track['copies'] + 1
        position = i
        for j in reversed(range(i)):
            if track:
                result = sorting_strategy(array[j], current, track)
            else:
                result = sorting_strategy(array[j], current)
            if result <= 0:
                break
            array[position] = array[position - 1]
            if track:
                track['copies'] = track['copies'] + 1
            position = position - 1
        array[position] = current
        if track:
            track['copies'] = track['copies'] + 1
    return array


def parse_text(path):
    with open(path) as text:
        lines = text.readlines()
        players = []
        for i in range(len(lines)):
            pair = lines[i].split("\t")
            pair[1] = pair[1].replace('\n', '')
            player = {'name': pair[0], 'score': pair[1]}
            players.append(player)
        return players


def update_score_tracker(score_tracker, results):
    if len(score_tracker) == 0:
        score_tracker.insert(0, results[0])
    for i in range(1, len(results), 1):
        for j in range((len(score_tracker)), 0, -1):
            result = sort_in_ascending(results[i]['score'], score_tracker[j - 1]['score'])
            if result < 0:
                if j == len(score_tracker):
                    score_tracker.append(score_tracker[j - 1])
                else:
                    score_tracker[j] = score_tracker[j - 1]
                score_tracker[j - 1] = results[i]
            if result > 0:
                if j == len(score_tracker):
                    score_tracker.append(results[i])
                    break
    return score_tracker


def print_top_ten(score_tracker):
    print("\n")
    print("********** Top 10 Players **********")
    for i in range(0, 10, 1):
        result = str(i + 1) + ' ' + score_tracker[i]['name'] + ' ' + score_tracker[i]['score']
        print(result)
