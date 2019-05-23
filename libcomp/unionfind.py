import sys
sys.setrecursionlimit(10000000)
class UnionFindTree:
    def __init__(self, n):
        self.nodes = list(range(n+1))
    def find(self, x):
        if self.nodes[x] == x:
            return x
        parent = self.find(self.nodes[x])
        self.nodes[x] = parent
        return parent
    def unite(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        self.nodes[a] = self.nodes[b]
    def is_same(self, a, b):
        return self.find(a) == self.find(b)
