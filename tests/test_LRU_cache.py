from algs.LRUCache import LRUCache

pokemon = ['bulbasaur', 'ivysaur', 'venusaur', 'charmander', 'charmeleon', 'charizard', 'squirtle', 'wartortle',
           'blastoise', 'caterpie', 'metapod', 'butterfree', 'weedle', 'kakuna', 'beedrill', 'pidgey', 'pidgeotto',
           'pidgeot', 'rattata', 'raticate', 'spearow', 'fearow', 'ekans', 'arbok', 'pikachu', 'raichu', 'sandshrew',
           'sandslash', 'nidoranF', 'nidorina', 'nidoqueen', 'nidoranM', 'nidorino', 'kidoking', 'clefairy', 'clefable',
           'vulpix', 'ninetales', 'jigglypuff', 'wigglytuff', 'zubat', 'golbat', 'oddish', 'gloom', 'vileploom',
           'paras', 'parasect', 'venonat', 'venomoth', 'diglett']


def test_LRU_cache_returns_value_from_key_when_not_present():
    cache = LRUCache()

    def func(key):
        return 'strawberry'

    result = cache.get('banana', func)
    assert result == 'strawberry'


def test_LRU_cache_returns_value_from_key_when_present():
    cache = LRUCache()

    def func(key):
        return 'strawberry'

    cache.get('banana', func)
    result = cache.get('banana', func)
    assert result == 'strawberry'


def test_LRU_cache_removes_oldest_value_at_50():
    cache = LRUCache()

    def func(key):
        return 'Ash Ketchum'

    for monster in pokemon:
        cache.get(monster, func)

    assert cache.get('dugtrio', func) == 'Ash Ketchum'
    assert cache.size == 50
    assert 'bulbasaur' not in str(cache.hash_table.data)
