from itertools import product
N,C=map(int, input().split())
cost=[[int(st) for st in input().split()] for _ in range(C)]
count={0: {}, 1: {}, 2: {}}
for y in range(N):
    for x, v in enumerate(map(int, input().split())):
        rest = (x+y) % 3
        count[rest][v] = 1 + count[rest].get(v, 0)
mincost = 9223372036854775807
for cc in product(*[range(1, C+1)]*3):
    if cc[0] != cc[1] and cc[0] != cc[2] and cc[1] != cc[2]:
        sumcost = 0
        for i in range(3):
            for cl, cnt in count[i].items():
                sumcost += cnt*cost[cl-1][cc[i]-1]
        mincost = min(sumcost, mincost)
print(mincost)
