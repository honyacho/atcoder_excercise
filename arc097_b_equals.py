N,M=map(int, input().split())
inseq=list(map(int, input().split()))

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

union = UnionFindTree(N)
for j in range(M): 
    union.unite(*[int(i) for i in input().split()])

res = 0
for i, v in enumerate(inseq, start=1):
    if union.is_same(i, v):
        res += 1
print(res)
