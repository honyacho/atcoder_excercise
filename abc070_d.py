import sys
sys.setrecursionlimit(10**7)
N=int(input())

NODES={}
for i in range(N-1):
    a,b,c=map(int,input().split())
    if not a in NODES: NODES[a] = []
    if not b in NODES: NODES[b] = []
    NODES[a].append((b, c))
    NODES[b].append((a, c))

Q,K=map(int,input().split())
MP=[-1]*(N+1)
MP[K]=0
def dfs(k):
    for i, c in NODES[k]:
        if MP[i] == -1:
            MP[i] = MP[k] + c
            dfs(i)

dfs(K)
# print(MP)
for l,r in [tuple(map(int,input().split())) for _ in range(Q)]:
    print(MP[l]+MP[r])
