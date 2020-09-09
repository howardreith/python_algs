from algs.binary_tree import BinaryTree
from algs.binary_tree_node import BinaryTreeNode


def test_binary_tree_can_be_created_with_proper_parameters():
    new_node = BinaryTreeNode(1)
    result = BinaryTree(new_node)
    assert result.get_root() == new_node


def test_binary_tree_insert_node_sets_node_to_root_when_there_is_no_root():
    new_node = BinaryTreeNode(1)
    tree = BinaryTree()
    tree.insert_node(new_node)
    assert tree.get_root() == new_node


def test_binary_tree_insert_node_properly_connects_new_left_and_root_when_root_left_empty():
    root_node = BinaryTreeNode(5)
    new_node = BinaryTreeNode(3)
    tree = BinaryTree(root_node)
    tree.insert_node(new_node)
    assert new_node.get_parent() == root_node
    assert root_node.get_left() == new_node


def test_binary_tree_insert_node_moves_nodes_down_left_path():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(3)
    new_node = BinaryTreeNode(1)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.insert_node(new_node)
    assert root_node.get_left() == child_node
    assert child_node.get_parent() == root_node
    assert new_node.get_parent() == child_node
    assert child_node.get_left() == new_node


def test_binary_tree_insert_node_properly_connects_new_right_and_root_when_root_right_empty():
    root_node = BinaryTreeNode(5)
    new_node = BinaryTreeNode(7)
    tree = BinaryTree(root_node)
    tree.insert_node(new_node)
    assert new_node.get_parent() == root_node
    assert root_node.get_right() == new_node


def test_binary_tree_insert_node_moves_nodes_down_right_path():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(7)
    new_node = BinaryTreeNode(9)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.insert_node(new_node)
    assert root_node.get_right() == child_node
    assert child_node.get_parent() == root_node
    assert new_node.get_parent() == child_node
    assert child_node.get_right() == new_node


def test_binary_tree_insert_can_zig_zag_starting_left():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(3)
    new_node = BinaryTreeNode(4)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.insert_node(new_node)
    assert root_node.get_left() == child_node
    assert child_node.get_parent() == root_node
    assert new_node.get_parent() == child_node
    assert child_node.get_right() == new_node


def test_binary_tree_insert_can_zig_zag_starting_right():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(7)
    new_node = BinaryTreeNode(6)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.insert_node(new_node)
    assert root_node.get_right() == child_node
    assert child_node.get_parent() == root_node
    assert new_node.get_parent() == child_node
    assert child_node.get_left() == new_node


def test_search_returns_root_when_value_at_root():
    new_node = BinaryTreeNode(1)
    tree = BinaryTree(new_node)
    result = tree.search(1)
    assert result == new_node


def test_search_returns_none_when_not_present():
    new_node = BinaryTreeNode(1)
    tree = BinaryTree(new_node)
    result = tree.search(2)
    assert result == None


def test_search_returns_appropriate_node_to_left():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(3)
    new_node = BinaryTreeNode(4)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.insert_node(new_node)
    result = tree.search(4)
    assert result == new_node


def test_search_returns_appropriate_node_to_right():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(7)
    new_node = BinaryTreeNode(6)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.insert_node(new_node)
    result = tree.search(6)
    assert result == new_node

def test_delete_node_deletes_a_node_with_no_children_left():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(3)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.delete_node(3)
    assert root_node.get_left() == None


def test_delete_node_deletes_a_node_with_no_children_right():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(7)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.delete_node(7)
    assert root_node.get_right() == None


def test_delete_node_sets_parent_nodes_left_to_nodes_left_when_only_left():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(3)
    test_node = BinaryTreeNode(1)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.insert_node(test_node)
    tree.delete_node(3)
    assert root_node.get_left() == test_node
    assert test_node.get_parent() == root_node


def test_delete_node_sets_parent_nodes_left_to_nodes_right_when_only_right():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(3)
    test_node = BinaryTreeNode(4)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.insert_node(test_node)
    tree.delete_node(3)
    assert root_node.get_left() == test_node
    assert test_node.get_parent() == root_node


def test_delete_node_sets_parent_nodes_right_to_nodes_right_when_only_right():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(7)
    test_node = BinaryTreeNode(9)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.insert_node(test_node)
    tree.delete_node(7)
    assert root_node.get_right() == test_node
    assert test_node.get_parent() == root_node


def test_delete_node_sets_parent_nodes_right_to_nodes_left_when_only_left():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(7)
    test_node = BinaryTreeNode(6)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.insert_node(test_node)
    tree.delete_node(7)
    assert root_node.get_right() == test_node
    assert test_node.get_parent() == root_node


def test_delete_node_sets_node_to_minimum():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(3)
    left_node = BinaryTreeNode(2)
    right_node = BinaryTreeNode(4)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    tree.insert_node(left_node)
    tree.insert_node(right_node)
    tree.delete_node(3)
    assert root_node.get_left().get_value() == 4
    assert root_node.get_left() == child_node
    assert child_node.get_value() == 4
    assert child_node.get_right() is None
    assert child_node.get_left() == left_node
    assert left_node.get_parent() == child_node
    assert left_node.get_value() == 2
    assert left_node.get_parent().get_value() == 4


def test_find_right_minimum_returns_root_node_when_no_rights():
    root_node = BinaryTreeNode(5)
    child_node = BinaryTreeNode(3)
    tree = BinaryTree(root_node)
    tree.insert_node(child_node)
    result = tree.find_right_minimum(root_node)
    assert result == root_node


def test_find_right_minimum_returns_right_minimum_in_shallow_example():
    root_node = BinaryTreeNode(5)
    left_node = BinaryTreeNode(3)
    right_node = BinaryTreeNode(7)
    tree = BinaryTree(root_node)
    tree.insert_node(left_node)
    tree.insert_node(right_node)
    result = tree.find_right_minimum(root_node)
    assert result == right_node


def test_find_right_minimum_returns_right_minimum_in_deep_example():
    root_node = BinaryTreeNode(5)
    left_node = BinaryTreeNode(3)
    right_node = BinaryTreeNode(9)
    deep_right_right_node = BinaryTreeNode(8)
    deep_right_left_node = BinaryTreeNode(11)
    tree = BinaryTree(root_node)
    tree.insert_node(left_node)
    tree.insert_node(right_node)
    tree.insert_node(deep_right_left_node)
    tree.insert_node(deep_right_right_node)
    result = tree.find_right_minimum(root_node)
    assert result == deep_right_right_node
