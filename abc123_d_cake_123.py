from heapq import heappop, heappush

X,Y,Z,K = map(int, input().split())
xs = [int(x) for x in input().split()]
ys = [int(y) for y in input().split()]
zs = [int(z) for z in input().split()]
xs.sort()
ys.sort()
zs.sort()
xs.reverse()
ys.reverse()
zs.reverse()

def bfs(max = 3000):
    count = 0
    pq = []
    checked = {}

    heappush(pq, (-(xs[0]+ys[0]+zs[0]), (0,0,0)))
    checked[(0,0,0)] = 1
    while count < max:
        value, (x, y, z) = heappop(pq)
        print(-value)
        count += 1
        if x+1 < X and not (x+1, y, z) in checked:
            checked[(x+1, y, z)] = 1
            heappush(pq, (-(xs[x+1]+ys[y]+zs[z]), (x+1, y, z)))
        if y+1 < Y and not (x, y+1, z) in checked:
            checked[(x, y+1, z)] = 1
            heappush(pq, (-(xs[x]+ys[y+1]+zs[z]), (x, y+1, z)))
        if z+1 < Z and not (x, y, z+1) in checked:
            checked[(x, y, z+1)] = 1
            heappush(pq, (-(xs[x]+ys[y]+zs[z+1]), (x, y, z+1)))

bfs(K)
