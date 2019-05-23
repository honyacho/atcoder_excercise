import sys
sys.setrecursionlimit(10000000)
N,K=map(int, input().split())

class UnionFindTree:
    def __init__(self, n):
        self.nodes = list(range(n+10))
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

uf = UnionFindTree(N)
for i in range(K):
    i,j,k=map(int, input().split())
    uf.unite(i,j)

st = set()
for i in range(1,N+1):
    par = uf.find(i)
    st.add(par)

print(len(st))
