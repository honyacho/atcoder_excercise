from collections import deque
from itertools import product
H,W=map(int,input().split())
inl=[input()for _ in range(H)]
checked=set([])
lis=[(1,0),(0,1),(-1,0),(0,-1)]
fifo = deque([])
def bfs(i,j):
    fifo.append((i,j))
    checked.add((i,j))
    cntBlack = 0
    cntWhite = 0
    while fifo:
        i,j = fifo.popleft()
        if inl[i][j] == '.': cntWhite += 1
        else: cntBlack += 1
        for di,dj in lis:
            if i+di>=0 and i+di<H and j+dj>=0 and j+dj<W and not (i+di,j+dj) in checked and inl[i][j]!=inl[i+di][j+dj]:
                checked.add((i+di, j+dj))
                fifo.append((i+di, j+dj))
    return cntBlack*cntWhite

res = 0
for i,j in product(range(H),range(W)): res += bfs(i,j) if not (i,j) in checked else 0
print(res)
