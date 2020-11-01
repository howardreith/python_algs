class BloomFilter(object):
    def __init__(self, size, functions):
        self.bit_vector_size = size
        self.functions = functions
        self.data = [0 for _ in range(size)]

    def insert(self, key):
        for func in self.functions:
            index = func(key, self.bit_vector_size)
            self.data[index] = 1

    def lookup(self, key):
        for func in self.functions:
            index = func(key, self.bit_vector_size)
            if self.data[index] == 0:
                return False
        return True
