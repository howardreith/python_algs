import copy

from algs.romeo_and_juliet import RomeoAndJuliet

text = '../txt_files/romeojuliet.txt'


def test_rome_and_juliet_parses_text():
    rj = RomeoAndJuliet(copy.deepcopy(text))
    expected_characters = ['Lord Montague', 'Lady Montague', 'Lady Capulet', 'Lord Capulet', 'Friar John', 'Apothecary',
                           'Nurse', 'Friar Laurence', 'Benvolio', 'Prince', 'Paris', 'Juliet', 'Tybalt', 'Romeo',
                           'Mercutio']
    assert rj.unique_characters == expected_characters
    expected_kin_list = ['Lord Montague\tkin\tRomeo', 'Lady Montague\tkin\tRomeo\n', 'Lady Capulet\tkin\tJuliet\n',
                         'Lord Capulet\tkin\tJuliet\n', 'Paris\tkin\tPrince\n', 'Tybalt\tkin\tJuliet\n']
    assert rj.kin_list == expected_kin_list


def test_romeo_and_juliet_creates_and_prints_union_finds():
    rj = RomeoAndJuliet(copy.deepcopy(text))
    rj.create_union_finds_for_chars()
    assert rj.set[0]['name'] == 'Mercutio'
    assert rj.set[0]['rank'] == 0
    assert rj.set[2]['name'] == 'Tybalt'
    assert rj.set[2]['parent']['name'] == 'Juliet'
    assert rj.set[2]['parent']['rank'] == 1
