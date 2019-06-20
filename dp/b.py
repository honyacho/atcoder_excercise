INTMAX = 9223372036854775807
def LI(): return [int(x) for x in input().split()]
def II(): return int(input())

N,K=LI()
INL=LI()
dp = [INTMAX]*N
dp[0] = 0

for i in range(0,N):
    for j in range(1,K+1):
        k = i+j
        if k < N:
            dp[k] = min(dp[k], dp[i]+abs(INL[k]-INL[i]))

# print(dp)
print(dp[N-1])
