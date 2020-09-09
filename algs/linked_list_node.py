class LinkedListNode(object):
    def __init__(self, value, next_node, previous_node):
        self.value = value
        self.next_node = next_node
        self.previous_node = previous_node

    def get_value(self):
        return self.value

    def set_value(self, value):
        self.value = value

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_previous(self):
        return self.previous_node

    def set_previous(self, previous_node):
        self.previous_node = previous_node
