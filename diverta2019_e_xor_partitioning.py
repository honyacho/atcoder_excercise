N=int(input())
INSEQ=list(map(int,input().split()))
INSEQ_acc=[0]*(N+1)
div=10**9+7

for i in range(N):
    INSEQ_acc[i+1] = INSEQ_acc[i]^INSEQ[i]

last=INSEQ_acc[-1]
same = []
for i in range(N+1):
    if INSEQ_acc[i] == last:
        same.append(i)

print(same)
res = 1
for i in range(len(same)-1):
    res *= (same[i+1] - same[i] + 1)

print((res-1)%div)
