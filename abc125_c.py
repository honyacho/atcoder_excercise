N=int(input())
nums = [int(i) for i in input().split()]

def gcd(x, y):
    if x < y:
        x = x ^ y
        y = x ^ y
        x = x ^ y
    div = x % y
    while div != 0:
        x = y
        y = div
        div = x % y
    return y

memo = {}
memo[(0, 1)] = nums[0]
memo[(N-1, N)] = nums[N-1]

for i in range(2, N+1):
    memo[(0, i)] = gcd(memo[(0, i - 1)], nums[i-1])

for i in reversed(range(0, N-1)):
    memo[(i, N)] = gcd(memo[(i + 1, N)], nums[i])

res = 1
for i in range(1, N-1):
    res = max(res, gcd(memo[(0, i)], memo[(i+1, N)]))

res = max(res, memo[(0, N-1)])
res = max(res, memo[(1, N)])

print(res)
