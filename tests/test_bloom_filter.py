import math

from algs.bloom_filter import BloomFilter
from algs.hashes import hash_djb2, ord_hash


def djb2(key, size):
    a = 0.6180339887
    h = hash_djb2(key)
    return math.floor(size * (h * a % 1))


def test_bloom_filter_can_be_created_with_proper_params():
    bloom_filter = BloomFilter(5, [djb2, ord_hash])
    assert bloom_filter is not None


def test_bloom_filter_insert_adds_to_list():
    bloom_filter = BloomFilter(10, [djb2, ord_hash])
    bloom_filter.insert("banana")
    assert bloom_filter.data == [0, 1, 0, 0, 0, 0, 0, 0, 0, 1]


def test_lookup_returns_true_when_value_present():
    bloom_filter = BloomFilter(10, [djb2, ord_hash])
    bloom_filter.insert("banana")
    result = bloom_filter.lookup('banana')
    assert result is True


def test_lookup_returns_false_when_value_absent():
    bloom_filter = BloomFilter(10, [djb2, ord_hash])
    bloom_filter.insert("banana")
    result = bloom_filter.lookup('strawberry')
    assert result is False
