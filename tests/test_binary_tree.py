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
