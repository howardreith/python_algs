from algs.hash_table import HashTable
from algs.hashes import hash_djb2


def test_hash_table_can_be_created_with_proper_parameters():
    hash_function = hash_djb2
    result = HashTable(10, hash_function)
    assert result.data == [[], [], [], [], [], [], [], [], [], []]
    assert result.size == 10
    assert result.max_size == 110


def test_put_adds_key_value_pair():
    hash_function = hash_djb2
    hash_table = HashTable(10, hash_function)
    hash_table.put('banana', 'strawberry')
    expected_kvp = {'banana': 'strawberry'}
    assert hash_table.data[1][0] == expected_kvp

def test_put_adds_multiple_key_value_pairs():
    hash_function = hash_djb2
    hash_table = HashTable(10, hash_function)
    hash_table.put('banana', 'strawberry')
    expected_kvp = {'banana': 'strawberry'}
    assert hash_table.data[1][0] == expected_kvp
    hash_table.put('blueberry', 'apple')
    expected_kvp = {'blueberry': 'apple'}
    assert hash_table.data[3][0] == expected_kvp

def test_put_overrides_key_value_pair():
    hash_function = hash_djb2
    hash_table = HashTable(10, hash_function)
    hash_table.put('banana', 'strawberry')
    hash_table.put('banana', 'blueberry')
    expected_kvp = {'banana': 'blueberry'}
    assert hash_table.data[1][0] == expected_kvp

def test_get_returns_no_item_message_with_no_item():
    hash_function = hash_djb2
    hash_table = HashTable(10, hash_function)
    result = hash_table.get('StarWars')
    assert result == 'No item found at key StarWars'

def test_get_returns_value():
    hash_function = hash_djb2
    hash_table = HashTable(10, hash_function)
    hash_table.put('banana', 'strawberry')
    result = hash_table.get('banana')
    assert result == 'strawberry'

def test_remove_returns_no_item_message_with_no_item():
    hash_function = hash_djb2
    hash_table = HashTable(10, hash_function)
    result = hash_table.remove('StarWars')
    assert result == 'No item found at key StarWars'

def test_remove_deletes_value_at_key():
    hash_function = hash_djb2
    hash_table = HashTable(10, hash_function)
    hash_table.put('banana', 'strawberry')
    expected_kvp = {'banana': 'strawberry'}
    assert hash_table.data[1][0] == expected_kvp
    hash_table.remove('banana')
    assert len(hash_table.data[1]) == 0
