import collections
N=int(input())
inarr=[[int(j) for j in input().split()] for i in range(N-1)]
nodes={}

if N == 1:
    print("First")
    exit()

for i,j in inarr:
    if not i in nodes: nodes[i] = [j]
    else: nodes[i].append(j)
    if not j in nodes: nodes[j] = [i]
    else: nodes[j].append(i)

visited = {1}
queue = collections.deque([[1, 0]])
while queue:
    i, d = queue.popleft()
    for node in nodes[i]:
        if not node in visited:
            visited.add(node)
            queue += [[node, d + 1]]

visited = {i}
queue = collections.deque([[i, 0]])
while queue:
    i, d = queue.popleft()
    for node in nodes[i]:
        if not node in visited:
            visited.add(node)
            queue += [[node, d + 1]]

print('Second' if d%3 == 1 else 'First')
