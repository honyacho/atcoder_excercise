from collections import deque
N,M,T=map(int,input().split())
SCRS=[0]+list(map(int,input().split()))

inmap={}
inmaprev={}
for _ in range(M):
    a,b,c=map(int,input().split())
    if not a in inmap:
        inmap[a] = [(b,c)]
    else:
        inmap[a].append((b,c))
    if not b in inmaprev:
        inmaprev[b] = [(a,c)]
    else:
        inmaprev[b].append((a,c))

que = deque([])
visited1 = set([1])
que.append(1)
time1=[9223372036854775807 for i in range(N+1)]
time1[1]=0
while que:
    check = que.popleft()
    if check in inmap:
        for (i, time) in inmap[check]:
            time1[i] = min(time1[i], time + time1[check])
            if not i in visited1:
                visited1.add(i)
                que.append(i)

visited2 = set([1])
time2=[9223372036854775807 for i in range(N+1)]
time2[1]=0
que.append(1)
while que:
    check = que.popleft()
    if check in inmaprev:
        for (i, time) in inmaprev[check]:
            time2[i] = min(time2[i], time + time2[check])
            if not i in visited2:
                visited2.add(i)
                que.append(i)

# print(time1)
# print(time2)

res=0
for i in range(1,N+1): res = max(res,(T-time1[i]-time2[i])*SCRS[i])
print(res)
