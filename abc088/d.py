import queue
H,W=map(int, input().split())
inmap = [input() for _ in range(H)]

q = queue.Queue(2500)
q.put((0,0,1))
cood = [(1,0),(-1,0),(0,1),(0,-1)]
res = 0

visited = set((0,0))

while not q.empty():
    x,y,cnt=q.get(False)
    if x+1 == W and y+1 == H:
        res = cnt
        break
    for dx, dy in cood:
        if x+dx >= 0 and x+dx < W and y+dy >= 0 and y+dy < H:
            if inmap[y+dy][x+dx] != '#' and not (x+dx, y+dy) in visited:
                q.put((x+dx, y+dy, cnt+1))
                visited.add((x+dx, y+dy))

black = 0
for i in range(H):
    for j in range(W):
        if inmap[i][j] == '#':
            black += 1

# print((W-1, H-1) in visited)
if res == 0:
    print(-1)
else:
    print(H*W - black - res)
