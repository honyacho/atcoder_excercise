from collections import deque
H,W=map(int,input().split())
inmap=[input() for i in range(H)]
que = deque([],10000000)
# print(inmap)
checked = {}
for i in range(H):
    for j in range(W):
        if inmap[i][j] == '#':
            que.append((i,j,0))
            checked[(i,j)] = 0

df=[(1,0),(-1,0),(0,1),(0,-1)]
resmax = 0
while len(que):
    (i,j,k) = que.popleft()
    # print(i,j,k)
    for dy, dx in df:
        if i+dy >= 0 and i+dy<H and j+dx<W and j+dx >=0 and not (i+dy, j+dx) in checked:
            que.append((i+dy,j+dx,k+1))
            resmax = max(resmax, k+1)
            checked[(i+dy,j+dx)] = k+1

print(resmax)
