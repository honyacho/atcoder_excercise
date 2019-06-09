from collections import deque
N=int(input())

tree = {i: set() for i in range(1, N+1)}
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a].add(b)
    tree[b].add(a)

inl = list(map(int,input().split()))
inl.sort()

res = [0]*(N+1)
qu = deque([1])
res[1] = inl.pop()

while qu:
    i = qu.popleft()
    for j in tree[i]:
        if res[j] == 0:
            res[j] = inl.pop()
            qu.append(j)

print(sum(res[2:]))
for i in res[1:]:
    print(i, end=' ')
print('')
