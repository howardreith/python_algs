class BinaryTreeNode(object):
    def __init__(self, value, parent=None, left=None, right=None):
        self.value = value
        self.parent = parent
        self.left = left
        self.right = right

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_left(self):
        return self.left

    def set_left(self, left):
        self.left = left

    def get_right(self):
        return self.right

    def set_right(self, right):
        self.right = right
