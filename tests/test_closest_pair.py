import pytest

from algs.closest_pair import ClosestPair

text = '../txt_files/points.txt'


def test_closest_pair_1d_brute_force_finds_closest_pair():
    sut = ClosestPair()
    array = [1, 5, 9, 22, -5, 24]
    result = sut.closest_pair_1d_brute_force(array)
    assert result == 2


def test_closest_pair_1d_recursive_finds_closest_pair_left_side():
    sut = ClosestPair()
    array = [1, 5, 9, 22, -5, 24, -50, 100]
    result = sut.closest_pair_1d_recursive(array)
    assert result == 4


def test_closest_pair_1d_recursive_finds_closest_pair_right_side():
    sut = ClosestPair()
    array = [1, 5, 9, 22, -5, 24, 103, 100]
    result = sut.closest_pair_1d_recursive(array)
    assert result == 3


def test_closest_pair_1d_recursive_finds_closest_pair_middle():
    sut = ClosestPair()
    array = [1, 5, 9, 22, 21, 24, 103, 100]
    result = sut.closest_pair_1d_recursive(array)
    assert result == 1


def test_closest_pair_1d_divide_conquer_finds_closest_pair():
    sut = ClosestPair()
    array = [1, 5, 9, 22, 107, 100, -2]
    result = sut.closest_pair_1d_divide_conquer(array)
    assert result == 3


def test_distance_returns_the_hypotneuse():
    sut = ClosestPair()
    point1 = [2, 3]
    point2 = [-3, -3]
    result = sut.distance(point1, point2)
    assert result == pytest.approx(7.81, 0.1)
    point3 = [0, 0]
    point4 = [3, 4]
    result = sut.distance(point3, point4)
    assert result == 5


def test_sort_list_of_lists_by_n_index_sorts_list_by_1():
    sut = ClosestPair()
    array = [[0, 0], [1, 1], [5, 4], [-5, 3], [-10, -10]]
    result = sut.sort_list_of_lists_by_n_index(array, 1)
    assert result == [[-10, -10], [0, 0], [1, 1], [-5, 3], [5, 4]]


def test_sort_list_of_lists_by_n_index_sorts_list_by_0():
    sut = ClosestPair()
    array = [[0, 0], [1, 1], [5, 4], [-5, 3], [-10, -10]]
    result = sut.sort_list_of_lists_by_n_index(array, 0)
    assert result == [[-10, -10], [-5, 3], [0, 0], [1, 1], [5, 4]]


def test_closest_pair_brute_force_2d_finds_closest_pair():
    sut = ClosestPair()
    array = [[0, 0], [1, 1], [5, 4], [-5, 3], [-10, -10]]
    result = sut.closest_pair_2d_brute_force(array)
    assert result == pytest.approx(1.41, 0.1)


def test_closest_pair_2d_divide_conquer_finds_closest_distance():
    sut = ClosestPair()
    array = [[0, 0], [1, 1], [5, 4], [-5, 3], [-10, -10]]
    result = sut.closest_pair_2d_divide_conquer(array)
    assert result == pytest.approx(1.41, 0.1)


def test_parse_text_file_parses_text_file():
    sut = ClosestPair()
    result = sut.parse_text_file(text)
    assert result[0] == [-31924.60266, -43939.639951]
    assert result[-1] == [23304.877557, -20178.637174]


def test_closest_pair_2d_finds_closest_pair_in_challenge():
    sut = ClosestPair()
    array = sut.parse_text_file(text)
    result = sut.closest_pair_2d_divide_conquer(array)
    assert result == pytest.approx(0.068070, 0.00001)


def test_closest_pair_2d_allow_duplicate_x_finds_closest_pair():
    sut = ClosestPair()
    array = [[0, 0], [1, 1], [5, 4], [-5, 3], [-10, -10]]
    result = sut.closest_pair_2d_divide_conquer_allow_duplicate_x(array)
    assert result == pytest.approx(1.41, 0.1)
