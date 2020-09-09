class Array(object):
    def __init__(self, size, array_type=int):
        self.size = len(list(map(array_type, range(size))))
        self.arrayItems = [array_type(0)] * size  # initialize array with zeroes in all indexes
        self.type = array_type

    def get_size(self):
        return self.size

    def get_array_items(self):
        return self.arrayItems

    def get_type(self):
        return self.type

    def insert(self, position, value):
        if self.size < position:
            raise Exception('Could not insert. Array size is ' + str(self.size))
        else:
            for i in range(self.size - 2, position - 1, -1):
                self.arrayItems[i + 1] = self.arrayItems[i]
            self.arrayItems[position] = value

    def delete(self, position):
        if self.size < position:
            raise Exception('Could not delete. Array size is ' + str(self.size))
        else:
            for i in range(position, self.size - 1):
                print('I ran ' + str(i))
                self.arrayItems[i] = self.arrayItems[i + 1]
            self.arrayItems[position + 1] = 0

    def search(self, value):
        print(self.size)
        for i in range(self.size):
            if self.arrayItems[i] == value:
                return i
        return -1
