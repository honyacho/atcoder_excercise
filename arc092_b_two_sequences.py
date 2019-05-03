from bisect import bisect_left
N=int(input())
A=[int(i) for i in input().split()]
B=[int(i) for i in input().split()]
res = 0
for i in reversed(range(30)):
    higher, lower = 1<<(i+1), 1<<i
    for j in range(N):
        A[j] %= higher
        B[j] %= higher
    B.sort()
    loc_sum = 0
    for k in range(N):
        cnt = 0
        if lower-A[k] >= 0:
            cnt += bisect_left(B, higher-A[k]) - bisect_left(B, lower-A[k])                
        else:
            cnt += bisect_left(B, higher-A[k])
            cnt += bisect_left(B, higher) - bisect_left(B, higher + lower - A[k])
        loc_sum += cnt
    res += lower*(loc_sum&1)
print(res)
