class BinaryTree(object):
    def __init__(self, root=None):
        self.root = root

    def get_root(self):
        return self.root

    def search(self, value, current_node=None):
        if current_node is None:
            current_node = self.root

        if self.get_root().get_value() == value:
            print("Value is at root")
            return self.get_root()

        else:
            if current_node.get_value() == value:
                print('Value is present in tree')
                return current_node
            elif value < current_node.get_value() and current_node.get_left() is not None:
                print("Move Left")
                current_node = current_node.get_left()
                return self.search(value, current_node)
            elif value > current_node.get_value() and current_node.get_right() is not None:
                print("Move Right")
                current_node = current_node.get_right()
                return self.search(value, current_node)
            else:
                print("Key is not present in tree")
                return None

    def insert_node(self, new_node, current_node=None):
        if self.root is None:
            self.root = new_node
            return
        else:
            if current_node is None:
                current_node = self.get_root()
            if new_node.get_value() < current_node.get_value():
                if current_node.get_left() is None:
                    current_node.set_left(new_node)
                    new_node.set_parent(current_node)
                    return
                else:
                    current_node = current_node.get_left()
                    self.insert_node(new_node, current_node)
                    return
            else:
                if current_node.get_right() is None:
                    current_node.set_right(new_node)
                    new_node.set_parent(current_node)
                    return
                else:
                    current_node = current_node.get_right()
                    self.insert_node(new_node, current_node)
                    return

    def delete_node(self, value, current_node = None):
        if current_node == None:
            current_node = self.search(value)

        if current_node.get_value() == self.get_root().get_value():
            parent_node = self.get_root()
        else:
            parent_node = current_node.get_parent()

        # No Children
        if current_node.get_left() == None and current_node.get_right() == None:
            if value <= parent_node.get_value():
                parent_node.set_left(None)
            else:
                parent_node.set_right(None)

        # Single Left NOde


        # Single Right Node


        # Two Children