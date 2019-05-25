from collections import deque
N=int(input())

mp={}
for _ in range(N-1):
    i,j,w=map(int,input().split())
    if not i in mp:
        mp[i] = []
    if not j in mp:
        mp[j] = []
    mp[i].append((j,w))
    mp[j].append((i,w))


res = [-1 for _ in range(N+1)]
que = deque([])

que.append((1,0))
res[1]=0
while que:
    i, dist = que.popleft()
    for j, dist2 in mp[i]:
        if res[j] == -1:
            bw = (dist + dist2) % 2
            res[j] = bw
            que.append((j,bw))

for i in range(1, N+1):
    print(res[i])
