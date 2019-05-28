import heapq
N,M=map(int, input().split())
inl=list(map(int, input().split()))

modi = []
for i in range(M):
    b,c = map(int, input().split())
    modi.append((c,b))

modi.sort(reverse=True)
heapq.heapify(inl)

# print(modi)
for c, b in modi:
    for _ in range(b):
        v = heapq.heappop(inl)
        if v >= c:
            heapq.heappush(inl, v)
            break
        heapq.heappush(inl, c)

print(sum(inl))
