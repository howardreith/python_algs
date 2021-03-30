from algs.disjoint_set import DisjointSet


def find_index_of_object_with_value(array, value):
    i = 0
    for item in array:
        if item['name'] == value:
            return i
        else:
            i += 1


class RomeoAndJuliet(object):
    def __init__(self, text):
        self.unique_characters = []
        self.kin_list = []
        self.set = []
        self.parse_text(text)

    def parse_text(self, path):
        with open(path) as text:
            lines = text.readlines()
            kin_list = []
            for line in lines:
                if 'kin' in line:
                    kin_list.insert(0, line)
            self.kin_list = kin_list

            char_list = []
            for pair in lines:
                pair = pair.replace('kin', '').replace('knows', '').replace('\n', '').split('\t')
                while '' in pair:
                    pair.remove('')
                for char in pair:
                    if char not in char_list:
                        char_list.insert(0, char)
            self.unique_characters = char_list

    def create_union_finds_for_chars(self):
        disjoint_set = DisjointSet()
        for char in self.unique_characters:
            disjoint_set.make_set({'name': char})

        for pair in self.kin_list:
            parsed_pair = pair.replace('\n', '').split('\tkin\t')
            index1 = find_index_of_object_with_value(disjoint_set.data, parsed_pair[0])
            index2 = find_index_of_object_with_value(disjoint_set.data, parsed_pair[1])
            disjoint_set.union(disjoint_set.data[index1], disjoint_set.data[index2])

        self.set = disjoint_set.data
