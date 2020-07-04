# int(input())
N,K=list(map(int,input().split()))
inl = [int(input()) for i in range(N)]
inl.sort()

res = 1000000000000
for i in range(N-K+1):
    res = min(res, inl[i+K-1] - inl[i])

print(res)
