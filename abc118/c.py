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

N=int(input())
As = list(map(int,input().split()))
As.sort()

res = As[0]
for i in range(1, N):
    res = gcd(res, As[i])

print(res)
