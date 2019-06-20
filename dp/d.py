def LI(): return [int(x) for x in input().split()]
def II(): return int(input())

N,W=LI()
LIS=[tuple(LI()) for _ in range(N)]

DP = [[0]*(W+1) for i in range(N+1)]

for i,(w,v) in enumerate(LIS, 1):
    for wb in range(0, W+1):
        DP[i][wb] = DP[i-1][wb]
        if wb >= w :
            DP[i][wb] = max(DP[i][wb], DP[i-1][wb-w]+v)

print(DP[N][W])
