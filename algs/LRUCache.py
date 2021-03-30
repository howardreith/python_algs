from algs.hash_table import HashTable
from algs.hashes import hash_djb2


# Least recently accessed, not least recently inserted. D'oh.
# Heap - reprioritize when you insert, pop off the top when over 50

class LRUCache(object):
    def __init__(self):
        self.hash_table = HashTable(50, hash_djb2)
        self.time_tracker = []
        self.size = 0

    def get(self, key, func):
        result = self.hash_table.get(key)
        if result == 'No item found at key ' + key:
            if self.size == 50:
                key_to_remove = self.time_tracker[49]
                self.hash_table.remove(key_to_remove)
                del (self.time_tracker[-1])
                self.size = self.size - 1
            value = func(key)
            result = self.hash_table.put(key, value)
            self.time_tracker.insert(0, key)
            self.size = self.size + 1
        return result
