N,K=map(int, input().split())

res = 0
init = 1/N
for i in range(1, N+1):
    p = init
    while i < K:
        i *= 2
        p *= 0.5
    res += p
print(res)
