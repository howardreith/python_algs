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

    def find_right_minimum(self, current_node=None):
        if current_node is None:
            current_node = self.get_root()
        if current_node.get_right() is not None:
            current_node = current_node.get_right()
        else:
            return current_node
        if current_node.get_left() is not None:
            current_node = current_node.get_left()
            return self.find_right_minimum(current_node)
        else:
            return current_node

    def delete_node(self, value, current_node=None):
        if current_node is None:
            current_node = self.search(value)

        if current_node.get_value() == self.get_root().get_value():
            parent_node = self.get_root()
        else:
            parent_node = current_node.get_parent()

        # No Children
        if current_node.get_left() is None and current_node.get_right() is None:
            if value <= parent_node.get_value():
                parent_node.set_left(None)
            else:
                parent_node.set_right(None)
            return

        # Single Left Node
        elif current_node.get_right() is None and current_node.get_left() is not None:
            if current_node.get_left().get_value() < parent_node.get_value():
                parent_node.set_left(current_node.get_left())
                current_node.get_left().set_parent(parent_node)
            else:
                parent_node.set_right(current_node.get_left())
                current_node.get_left().set_parent(parent_node)
            return

        # Single Right Node
        elif current_node.get_right() is not None and current_node.get_left() is None:
            if current_node.get_right().get_value() > parent_node.get_value():
                parent_node.set_right(current_node.get_right())
                current_node.get_right().set_parent(parent_node)
            else:
                parent_node.set_left(current_node.get_right())
                current_node.get_right().set_parent(parent_node)
            return
        # Two Children
        elif current_node.get_left() is not None and current_node.get_right() is not None:
            minimum = self.find_right_minimum(current_node)
            current_node.set_value(minimum.get_value())
            if minimum.get_parent().get_right() == minimum:
                minimum.get_parent().set_right(None)
            else:
                minimum.get_parent().set_left(None)
            return
