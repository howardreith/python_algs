from algs.comparators import sort_in_ascending


def insertion_sort(array, sorting_strategy):
    sorted_list = []
    sorted_list.insert(0, array[0])
    for i in range(1, len(array), 1):
        for j in range((len(sorted_list)), 0, -1):
            result = sorting_strategy(array[i], sorted_list[j-1])
            if result < 0:
                if j == len(sorted_list):
                    sorted_list.append(sorted_list[j-1])
                else:
                    sorted_list[j] = sorted_list[j - 1]
                sorted_list[j - 1] = array[i]
            if result > 0:
                if j == len(sorted_list):
                    sorted_list.append(array[i])
                    break
    return sorted_list


def parse_text(text):
    lines = text.readlines()
    players = []
    for i in range(len(lines)):
        pair = lines[i].split("\t")
        pair[1] = pair[1].replace('\n', '')
        player = {}
        player['name'] = pair[0]
        player['score'] = pair[1]
        players.append(player)
    return players


def update_score_tracker(score_tracker, results):
    if (len(score_tracker) == 0):
        score_tracker.insert(0, results[0])
    for i in range(1, len(results), 1):
        for j in range((len(score_tracker)), 0, -1):
            result = sort_in_ascending(results[i]['score'], score_tracker[j-1]['score'])
            if result < 0:
                if j == len(score_tracker):
                    score_tracker.append(score_tracker[j-1])
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
        result = str(i+1) + ' ' + score_tracker[i]['name'] + ' ' + score_tracker[i]['score']
        print(result)
