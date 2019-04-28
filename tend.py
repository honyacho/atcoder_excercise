div = 998244353
N = int(input())
inputs = [int(input()) for i in range(N)]
inputs.sort()

memo = {}
def dp(n, r):
    for i in range(1, r):
        dp(n - 1, r)
    return 0
