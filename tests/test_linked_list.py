import pytest

from algs.linked_list import LinkedList
from algs.linked_list_node import LinkedListNode


def test_linked_list_can_be_created_with_proper_parameters():
    result = LinkedList()
    assert result.get_head() is None


def test_linked_list_can_set_and_get_head():
    node1 = LinkedListNode(1, None, None)
    node2 = LinkedListNode(2, None, node1)
    node1.set_next(node2)
    linked_list = LinkedList()
    linked_list.set_head(node1)
    assert linked_list.get_head() == node1


def test_linked_list_find_returns_minus_one_when_absent():
    node1 = LinkedListNode(1, None, None)
    node2 = LinkedListNode(2, None, node1)
    node1.set_next(node2)
    linked_list = LinkedList()
    linked_list.set_head(node1)
    result = linked_list.find(3)
    assert result == -1


def test_linked_list_find_returns_index_when_value_is_present():
    node1 = LinkedListNode(1, None, None)
    node2 = LinkedListNode(4, None, node1)
    node1.set_next(node2)
    linked_list = LinkedList()
    linked_list.set_head(node1)
    result = linked_list.find(4)
    assert result == 1


def test_linked_list_insert_raises_exception_when_index_too_high():
    node1 = LinkedListNode(1, None, None)
    node2 = LinkedListNode(4, None, node1)
    node1.set_next(node2)
    linked_list = LinkedList()
    linked_list.set_head(node1)
    new_node = LinkedListNode(6, None, None)
    with pytest.raises(Exception):
        linked_list.insert(4, new_node)


def test_linked_list_insert_adds_node_to_front_with_index_zero():
    node1 = LinkedListNode(2, None, None)
    node2 = LinkedListNode(4, None, node1)
    node1.set_next(node2)
    linked_list = LinkedList()
    linked_list.set_head(node1)
    new_node = LinkedListNode(1, None, None)
    linked_list.insert(0, new_node)
    assert linked_list.get_head() == new_node
    assert linked_list.get_head().get_next() == node1
    assert node1.get_previous() == new_node


def test_linked_list_insert_adds_node_at_appropriate_index():
    node1 = LinkedListNode(2, None, None)
    node2 = LinkedListNode(4, None, node1)
    node1.set_next(node2)
    linked_list = LinkedList()
    linked_list.set_head(node1)
    new_node = LinkedListNode(3, None, None)
    linked_list.insert(1, new_node)
    assert linked_list.get_head().get_next() == new_node
    assert new_node.get_previous() == node1
    assert node2.get_previous() == new_node
    assert new_node.get_next() == node2


def test_linked_list_insert_adds_node_at_last_index():
    node1 = LinkedListNode(2, None, None)
    node2 = LinkedListNode(4, None, node1)
    node1.set_next(node2)
    linked_list = LinkedList()
    linked_list.set_head(node1)
    new_node = LinkedListNode(5, None, None)
    linked_list.insert(2, new_node)
    assert new_node.get_previous() == node2
    assert node2.get_next() == new_node
    assert new_node.get_next() == None


def test_linked_list_delete_raises_exception_when_index_too_high():
    node1 = LinkedListNode(1, None, None)
    node2 = LinkedListNode(4, None, node1)
    node1.set_next(node2)
    linked_list = LinkedList()
    linked_list.set_head(node1)
    with pytest.raises(Exception):
        linked_list.delete(4)


def test_linked_list_delete_removes_head_with_index_zero():
    node1 = LinkedListNode(1, None, None)
    node2 = LinkedListNode(4, None, node1)
    node1.set_next(node2)
    linked_list = LinkedList()
    linked_list.set_head(node1)
    linked_list.delete(0)
    assert linked_list.get_head() == node2
    assert node2.get_previous() == None


def test_linked_list_delete_removes_node_with_given_index():
    node1 = LinkedListNode(1, None, None)
    node2 = LinkedListNode(4, None, node1)
    node3 = LinkedListNode(5, None, node2)
    node1.set_next(node2)
    node2.set_next(node3)
    linked_list = LinkedList()
    linked_list.set_head(node1)
    linked_list.delete(1)
    assert node1.get_next() == node3
    assert node3.get_previous() == node1


def test_linked_list_delete_removes_node_at_end_of_list():
    node1 = LinkedListNode(1, None, None)
    node2 = LinkedListNode(4, None, node1)
    node3 = LinkedListNode(5, None, node2)
    node1.set_next(node2)
    node2.set_next(node3)
    linked_list = LinkedList()
    linked_list.set_head(node1)
    linked_list.delete(2)
    assert node2.get_next() is None
