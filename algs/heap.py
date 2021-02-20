def default_priority_function(item1, item2):
    return item1 - item2


class Heap(object):
    def __init__(self, size, priority_function=default_priority_function):
        self.size = size
        self.items = [None] * size
        self.priorityFunction = priority_function
        self.lastItemIndex = 0

    def insert(self, item):
        if self.lastItemIndex == self.size:
            self.expand()
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

    def peek(self):
        return self.items[0]

    def get_size(self):
        return self.lastItemIndex

    def expand(self):
        if self.size == 0:
            self.items = [None]
            self.size = 1
        else:
            array_to_append = [None] * self.size
            self.items.extend(array_to_append)
            self.size = self.size * 2

    def delete(self, value):
        if value not in self.items:
            raise Exception('Value not in heap')
        index = self.items.index(value)
        del self.items[index]
        self.items.append(None)
        self.lastItemIndex = self.lastItemIndex - 1
        self.reprioritize(index)

    def bubble_up(self, index):
        while index != 0:
            parent_index = self.get_parent_index(index)
            if self.priorityFunction(self.items[index], self.items[parent_index]) <= 0:
                return
            self.items[index], self.items[parent_index] = self.items[parent_index], self.items[index]
            index = parent_index

    def bubble_down(self, index):
        # Investigate if you need a -1 after the self.lastItemIndex
        while self.get_child_index(index) < self.lastItemIndex:
            child_index = self.get_child_index(index)
            child_index = self.find_greatest_priority(child_index, child_index + 1)
            if self.priorityFunction(self.items[index], self.items[child_index]) >= 0:
                return
            self.items[index], self.items[child_index] = self.items[child_index], self.items[index]
            index = child_index

    def find_greatest_priority(self, x, y):
        if self.priorityFunction(self.items[x], self.items[y]) >= 0:
            return x
        return y

    def reprioritize(self, index):
        if index == 0:
            self.bubble_down(index)

        parent_index = self.get_parent_index(index)
        priority_result = self.priorityFunction(self.items[index], self.items[parent_index])
        if priority_result > 0:
            self.bubble_up(index)
        else:
            self.bubble_down(index)

    @staticmethod
    def get_parent_index(index):
        return int((index + 1) / 2 - 1)

    @staticmethod
    def get_right_child_index(index):
        return 2 * (index + 1)

    @staticmethod
    def get_left_child_index(index):
        return 2 * (index + 1) - 1

    @staticmethod
    def get_child_index(index):
        index = index + 1
        index = index << 1
        return index - 1
