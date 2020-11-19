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



# class DisjointSet(object):
#     def __init__(self, size):
#         if (size <= 0):
#             raise Exception('Invalid size.')
#         self.size = size
#         self.parent = [None] * (size + 1)
#         self.rank = [None] * (size + 1)
#
#     def make_set(self, obj):
#         self.parent[obj] = obj
#         self.rank[obj] = 0
#
#     def find(self, obj):
#         if obj != self.parent[obj]:
#             self.parent[obj] = self.find(self.parent[obj])
#         return self.parent[obj]
#
#     def union(self, obj1, obj2):
#         set1 = self.find(obj1)
#         set2 = self.find(obj2)
#         if set1 == set2:
#             return
#
#         if self.rank[set1] > self.rank[set2]:
#             self.parent[set2] = set1
#         else:
#             self.parent[set1] = set2
#             if self.rank[set1] == self.rank[set2]:
#                 self.rank[set2] += 1