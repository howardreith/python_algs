from algs.linked_list_node import LinkedListNode


class LinkedList(object):
    def __init__(self):
        self.head = None

    def get_head(self):
        return self.head

    def set_head(self, node):
        self.head = node

    def find(self, value):
        index = 0
        store = self.get_head()

        while store:
            if store.get_value() == value:
                return index

            index += 1
            store = store.get_next()

        return -1

    def insert(self, target_index, new_node):
        store = self.get_head()

        if target_index == 0:
            store.set_previous(new_node)
            new_node.set_next(store)
            self.set_head(new_node)
            return

        index = 0

        while index < target_index:
            previous = store
            store = store.get_next()
            index += 1

        if index == target_index:
            new_node.set_previous(previous)
            previous.set_next(new_node)
            if store:
                store.set_previous(new_node)
                new_node.set_next(store)
            return

        raise Exception('Index out of bounds')


    def delete(self, target_index):
        store = self.get_head()

        if target_index == 0:
            self.set_head(store.get_next())
            store.get_next().set_previous(None)
            return

        index = 0

        while index < target_index:
            store = store.get_next()
            index += 1

        if index == target_index:
            theNext = store.get_next()
            previous = store.get_previous()
            if theNext:
                theNext.set_previous(previous)
                previous.set_next(theNext)
            else:
                previous.set_next(None)
            return

        raise Exception('Index out of bounds')
