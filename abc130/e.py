DIVS = 1000000007
def LI(): return [int(x) for x in input().split()]

N,M=LI()
SS=LI()
TT=LI()

dp=[[0]*(M+1) for _ in range(N+1)]

for i in range(1,N+1):
    for j in range(1,M+1):
        if SS[i-1] != TT[j-1]:
            dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1]
        else:
            dp[i][j] = (dp[i-1][j] + dp[i][j-1] + 1) % DIVS

print((dp[N][M]+1)%DIVS)