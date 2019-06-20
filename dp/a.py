INTMAX = 9223372036854775807
def LI(): return [int(x) for x in input().split()]
def II(): return int(input())

N=II()
INL=LI()
dp=[INTMAX]*N
dp[0] = 0
dp[1] = abs(INL[1]-INL[0])

for i in range(2, N):
    dp[i] = min(dp[i-1]+abs(INL[i-1]-INL[i]), dp[i-2]+abs(INL[i-2]-INL[i]))

print(dp[N-1])
