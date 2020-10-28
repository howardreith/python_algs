class Heap(object):
    def __init__(self, size, priority_function):
        self.size = size
        self.items = [None] * (size + 1)
        self.priorityFunction = priority_function
        self.lastItemIndex = 0

    def insert(self, item):
        if self.lastItemIndex == self.size:
            raise Exception('Stack overflow')
        self.items[self.lastItemIndex] = item
        bubble_up_index = self.lastItemIndex
        self.lastItemIndex += 1
        self.bubble_up(bubble_up_index)

    def extract(self):
        if self.lastItemIndex == 0:
            raise Exception('Stack underflow')
        return_value = self.items[0]
        self.lastItemIndex = self.lastItemIndex - 1
        self.items[0] = self.items[self.lastItemIndex]
        bubble_down_index = 0
        self.bubble_down(bubble_down_index)
        return return_value

    def bubble_up(self, index):
        while index != 0:
            parent_index = self.get_parent_index(index)
            if self.priorityFunction(self.items[index], self.items[parent_index]) <= 0:
                return
            store = self.items[index]
            self.items[index] = self.items[parent_index]
            self.items[parent_index] = store
            index = parent_index

    def bubble_down(self, index):
        # Investigate if you need a -1 after the self.lastItemIndex
        while self.get_right_child_index(index) < self.lastItemIndex:
            left = self.get_left_child_index(index)
            right = self.get_right_child_index(index)
            if self.priorityFunction(self.items[left], self.items[right]) >= 1:
                child_index = left
            else:
                child_index = right
            if self.priorityFunction(self.items[index], self.items[child_index]) >= 0:
                return
            store = self.items[index]
            self.items[index] = self.items[child_index]
            self.items[child_index] = store
            index = child_index

    @staticmethod
    def get_parent_index(index):
        return int((index + 1) / 2 - 1)

    @staticmethod
    def get_right_child_index(index):
        return 2 * (index + 1)

    @staticmethod
    def get_left_child_index(index):
        return 2 * (index + 1) - 1
