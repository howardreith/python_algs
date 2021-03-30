import math

A = 0.6180339887


class HashTable(object):
    def __init__(self, size, hash_function):
        self.max_size = size + 100
        self.size = size
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
            key_value_pair_index = self.get_key_value_pair_index_from_list(key, bucket)
            if key_value_pair_index != len(bucket):
                bucket[key_value_pair_index][str(key)] = value
            else:
                bucket.insert(0, {str(key): value})
            return value
        else:
            key_value_pair = {str(key): value}
            bucket.insert(0, key_value_pair)
            return value

    def get(self, key):
        index = self.get_index(key)
        bucket = self.data[index]
        key_is_in_bucket = False
        for dic in bucket:
            if key in dic:
                key_is_in_bucket = True
        if bucket is None or len(bucket) == 0 or not key_is_in_bucket:
            return 'No item found at key ' + key
        else:
            key_value_pair_index = self.get_key_value_pair_index_from_list(key, bucket)
            return bucket[key_value_pair_index][str(key)]

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
            del (bucket[key_value_pair_index])

    @staticmethod
    def get_key_value_pair_index_from_list(key, bucket):
        key_value_pair_index = len(bucket)
        for i, dictionary in enumerate(bucket, start=0):
            if key in dictionary:
                key_value_pair_index = i
        return key_value_pair_index
