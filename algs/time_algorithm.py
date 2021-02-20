import time

from algs.comparators import sort_in_ascending
from algs.merge_sort import parse_text

text = '../txt_files/sort.txt'

def test_alg_2(func):
    array = parse_text(text)
    startTime = time.time()
    func(array)
    executionTime = (time.time() - startTime)
    return executionTime

def time_algorithm(*args):
    # accept a function and pass in a lambda
    array = parse_text(text)
    startTime = time.time()
    if (len(args) == 1):
        args[0](array)
    elif (len(args) == 2):
        args[0](array, args[1])
    elif (len(args) == 3):
        args[0](array, args[1], args[2])
    elif (len(args) == 4):
        args[0](array, args[1], args[2], args[3])
    elif (len(args) == 5):
        args[0](array, args[1], args[2], args[3], args[4])
    executionTime = (time.time() - startTime)
    return executionTime

def time_matrix_algorithm(*args):
    # accept a function and pass in a lambda
    startTime = time.time()
    args[0](len(args[1]), args[1], args[2])
    executionTime = (time.time() - startTime)
    return executionTime