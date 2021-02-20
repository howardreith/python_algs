from operator import itemgetter
from algs.bubble_sort import bubble_sort
from algs.comparators import sort_in_ascending
from algs.insertion_sort import insertion_sort
from algs.merge_sort import parse_text, merge_sort
from algs.quick_sort import quick_sort, pivot_on_zero
from algs.selection_sort import selection_sort

from algs.time_algorithm import time_algorithm, test_alg_2

text = '../txt_files/sort.txt'


def test_measure_time_of_all_algs():
    results = []
    results.append({'Name': 'Quick Sort', 'value': time_algorithm(quick_sort, 0, 10000 - 1, sort_in_ascending, pivot_on_zero)})
    results.append({'Name': 'Merge Sort', 'value': time_algorithm(merge_sort, sort_in_ascending)})
    results.append({'Name': 'Insertion Sort', 'value': time_algorithm(insertion_sort, sort_in_ascending)})
    results.append({'Name': 'Selection Sort', 'value': time_algorithm(selection_sort, sort_in_ascending)})
    results.append({'Name': 'Bubble Sort', 'value': time_algorithm(bubble_sort, sort_in_ascending)})
    results.append({'Name': 'Python Internal Sort', 'value': time_algorithm(sorted)})
    sortedResults = sorted(results, key=itemgetter('value'))
    print('***********************')
    for result in sortedResults:
        print(result['Name'] + ': ' + str(result['value']))
    print('***********************')


def test_measure_time_of_all_algs2():
    results = []

    results.append(test_alg_2(lambda array: quick_sort(array, 0, 10000 - 1, sort_in_ascending, pivot_on_zero)))
    print(results)

    # results.append({'Name': 'Quick Sort', 'value': time_algorithm(quick_sort, 0, 10000 - 1, sort_in_ascending, pivot_on_zero)})
    # results.append({'Name': 'Merge Sort', 'value': time_algorithm(merge_sort, sort_in_ascending)})
    # results.append({'Name': 'Insertion Sort', 'value': time_algorithm(insertion_sort, sort_in_ascending)})
    # results.append({'Name': 'Selection Sort', 'value': time_algorithm(selection_sort, sort_in_ascending)})
    # results.append({'Name': 'Bubble Sort', 'value': time_algorithm(bubble_sort, sort_in_ascending)})
    # results.append({'Name': 'Python Internal Sort', 'value': time_algorithm(sorted)})
    # sortedResults = sorted(results, key=itemgetter('value'))
    # print('***********************')
    # for result in sortedResults:
    #     print(result['Name'] + ': ' + str(result['value']))
    # print('***********************')