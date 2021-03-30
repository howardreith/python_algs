def hash_djb2(s):
    my_hash = 5381
    for x in s:
        my_hash = ((my_hash << 5) + my_hash) + ord(x)
    return my_hash & 0xFFFFFFFF


def ord_hash(string, table_size):
    hash_val = 0
    for position in range(len(string)):
        hash_val = hash_val + ord(string[position])

    return hash_val % table_size
