import heapq
K = int(input())
visited=[0]*100001
visited[1]=1
queue=[(1,1)]

while queue and queue[0][1] != 0:
    cost, value = heapq.heappop(queue)
    cand1 = value*10 % K
    cand2 = (value+1) % K
    if not visited[cand1]:
        visited[cand1] = 1
        heapq.heappush(queue,(cost, cand1))
    if not visited[cand2]:
        visited[cand1] = 1
        heapq.heappush(queue,(cost+1, cand2))

print(queue[0][0])
