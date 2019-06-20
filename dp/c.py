def LI(): return [int(x) for x in input().split()]
def II(): return int(input())

N=II()
LIS=[LI() for i in range(N)]
DP = [[0,0,0] for i in range(N+1)]
for i, li in enumerate(LIS):
    for j in range(3):
        for k in range(3):
            if j != k:
                DP[i+1][k] = max(DP[i+1][k], DP[i][j]+li[k])

print(max(DP[N]))
