import time

from algs.merge_sort import parse_text

text = '../txt_files/sort.txt'


def test_alg_2(func):
    array = parse_text(text)
    start_time = time.time()
    func(array)
    execution_time = (time.time() - start_time)
    return execution_time


def time_algorithm(*args):
    # accept a function and pass in a lambda
    array = parse_text(text)
    start_time = time.time()
    if len(args) == 1:
        args[0](array)
    elif len(args) == 2:
        args[0](array, args[1])
    elif len(args) == 3:
        args[0](array, args[1], args[2])
    elif len(args) == 4:
        args[0](array, args[1], args[2], args[3])
    elif len(args) == 5:
        args[0](array, args[1], args[2], args[3], args[4])
    execution_time = (time.time() - start_time)
    return execution_time


def time_matrix_algorithm(*args):
    # accept a function and pass in a lambda
    start_time = time.time()
    args[0](len(args[1]), args[1], args[2])
    execution_time = (time.time() - start_time)
    return execution_time
