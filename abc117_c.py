import heapq
N,M=list(map(int,input().split()))
Xs = list(map(int,input().split()))
Xs.sort()

if N >= M:
    print(0)
    exit()

pq = []
for i in range(M-1):
    heapq.heappush(pq, Xs[i] - Xs[i+1])

for i in range(N-1):
    heapq.heappop(pq)

res = 0
while pq:
    res -= heapq.heappop(pq)

print(res)
