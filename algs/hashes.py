def hash_djb2(s):
    hash = 5381
    for x in s:
        hash = (( hash << 5) + hash) + ord(x)
    return hash & 0xFFFFFFFF


def ord_hash(string, table_size):
    hash_val = 0
    for position in range(len(string)):
        hash_val = hash_val + ord(string[position])

    return hash_val % table_size