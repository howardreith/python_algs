class DisjointSet(object):
    def __init__(self):
        self.data = []

    def make_set(self, obj):
        obj['parent'] = obj
        obj['rank'] = 0
        self.data.insert(0, obj)

    def find(self, obj):
        if obj['parent'] != obj:
            obj['parent'] = self.find(obj['parent'])
        return obj['parent']

    def union(self, obj1, obj2):
        set1 = self.find(obj1)
        set2 = self.find(obj2)
        if set1 == set2:
            return

        if set1['rank'] > set2['rank']:
            set2['parent'] = set1
        else:
            set1['parent'] = set2
            if set1['rank'] == set2['rank']:
                set2['rank'] += 1
