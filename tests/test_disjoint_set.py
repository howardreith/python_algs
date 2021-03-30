import pytest

from algs.disjoint_set import DisjointSet


def test_disjoint_set_can_be_created():
    result = DisjointSet()
    assert result.data == []


def test_make_set_creates_a_set():
    disjoint_set = DisjointSet()
    disjoint_set.make_set({'name': 'banana'})
    disjoint_set.make_set({'name': 'strawberry'})
    assert len(disjoint_set.data) == 2


def test_find_returns_obj_when_it_is_parent_obj():
    disjoint_set = DisjointSet()
    disjoint_set.make_set({'name': 'banana'})
    result = disjoint_set.find(disjoint_set.data[0])
    assert result == disjoint_set.data[0]


def test_union_joins_objects_in_set():
    disjoint_set = DisjointSet()
    disjoint_set.make_set({'name': 'banana'})
    disjoint_set.make_set({'name': 'strawberry'})
    disjoint_set.make_set({'name': 'blueberry'})
    disjoint_set.union(disjoint_set.data[0], disjoint_set.data[1])
    assert disjoint_set.data[0]['name'] == 'blueberry'
    assert disjoint_set.data[0]['parent']['name'] == 'strawberry'
    assert disjoint_set.data[0]['parent']['rank'] == 1
    assert disjoint_set.data[0]['rank'] == 0
