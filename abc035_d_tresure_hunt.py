import heapq
N,M,T=map(int,input().split())
SCRS=[0]+list(map(int,input().split()))

inmap={}
inmap_rev={}
prevs = [-1]*(N+1)
prevs_rev = [-1]*(N+1)
dist = [9223372036854775807]*(N+1)
dist_rev = [9223372036854775807]*(N+1)
dist[1] = 0
dist_rev[1] = 0

for _ in range(M):
    a,b,c=map(int,input().split())
    if not a in inmap:
        inmap[a] = []
    if not b in inmap_rev:
        inmap_rev[b] = []
    inmap[a].append((b,c))
    inmap_rev[b].append((a,c))

PQ = [(0, 1)]
while PQ:
    _, vf = heapq.heappop(PQ)
    for vt, cost in inmap.get(vf, []):
        new_dist = dist[vf] + cost
        if new_dist < dist[vt]:
            dist[vt] = new_dist
            prevs[vt] = vf
            heapq.heappush(PQ, (new_dist, vt))

PQ = [(0, 1)]
while PQ:
    _, vf = heapq.heappop(PQ)
    for vt, cost in inmap_rev.get(vf, []):
        new_dist = dist_rev[vf] + cost
        if new_dist < dist_rev[vt]:
            dist_rev[vt] = new_dist
            prevs_rev[vt] = vf
            heapq.heappush(PQ, (new_dist, vt))

# print(dist)
# print(dist_rev)

res = 0
for i in range(1, N+1):
    res = max(res, SCRS[i]*(T-(dist[i]+dist_rev[i])))
print(res)
