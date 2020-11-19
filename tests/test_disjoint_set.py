import pytest

from algs.disjoint_set import DisjointSet


def test_disjoint_set_can_be_created():
    result = DisjointSet()
    assert result.data == []


def test_make_set_creates_a_set():
    set = DisjointSet()
    set.make_set({'name': 'banana'})
    set.make_set({'name': 'strawberry'})
    assert len(set.data) == 2


def test_find_returns_obj_when_it_is_parent_obj():
    set = DisjointSet()
    set.make_set({'name': 'banana'})
    result = set.find(set.data[0])
    assert result == set.data[0]


def test_union_joins_objects_in_set():
    set = DisjointSet()
    set.make_set({'name': 'banana'})
    set.make_set({'name': 'strawberry'})
    set.make_set({'name': 'blueberry'})
    set.union(set.data[0], set.data[1])
    assert set.data[0]['name'] == 'blueberry'
    assert set.data[0]['parent']['name'] == 'strawberry'
    assert set.data[0]['parent']['rank'] == 1
    assert set.data[0]['rank'] == 0
