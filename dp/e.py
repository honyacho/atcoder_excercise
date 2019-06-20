def LI(): return [int(x) for x in input().split()]
def II(): return int(input())

N,W=LI()
INL = [tuple(LI()) for i in range(N)]
DP=[[10**18]*100001 for _ in range(N+1)]
DP[0][0] = 0

for i, (w, v) in enumerate(INL, 1):
    for j in range(100001):
        DP[i][j] = min(DP[i-1][j], DP[i][j])
        if (j+v) <= 100000:
            DP[i][j+v] = min(DP[i-1][j+v], DP[i-1][j]+w)

res = 0
for v, w in enumerate(DP[N]):
    if w <= W:
        res = max(res, v)

print(res)
