import math

from algs.linked_list import LinkedList

A = 0.6180339887


class HashTable(object):
    def __init__(self, size, hash_function):
        self.max_size = size + 100
        self.size = size
        # self.keys = []
        self.hash_function = hash_function
        self.data = [[] for _ in range(size)]

    def get_index(self, key):
        h = self.hash_function(key)
        return math.floor(self.size * (h * A % 1))

    def put(self, key, value):
        index = self.get_index(key)
        bucket = self.data[index]
        if bucket is None:
            self.data[index] = []
            bucket = self.data[index]
        if len(bucket) > 0:
            key_value_pair = self.get_key_value_pair_from_list(key, bucket)
            key_value_pair[str(key)] = value
        else:
            key_value_pair = {str(key): value}
            bucket.append(key_value_pair)

    def get(self, key):
        index = self.get_index(key)
        bucket = self.data[index]
        if bucket is None or len(bucket) == 0:
            return 'No item found at key ' + key
        else:
            return self.get_key_value_pair_from_list(key, bucket)[str(key)]

    def remove(self, key):
        index = self.get_index(key)
        bucket = self.data[index]
        if bucket is None or len(bucket) == 0:
            return 'No item found at key ' + key
        else:
            key_value_pair_index = len(bucket)
            for i, dict in enumerate(bucket, start=0):
                if key in dict:
                    key_value_pair_index = i
            del(bucket[key_value_pair_index])

    @staticmethod
    def get_key_value_pair_from_list(key, bucket):
        key_value_pair_index = len(bucket)
        for i, dict in enumerate(bucket, start=0):
            if key in dict:
                key_value_pair_index = i
        return bucket[key_value_pair_index]

# TODO
# https://github.com/calebmadrigal/algorithms-in-python/blob/master/hashtable.py
#
#