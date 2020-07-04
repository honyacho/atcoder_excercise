import heapq

N,K=map(int,input().split())
inl = list(map(int,input().split()))

pq = []
max_score = 0
# 左からi個
for i in range(min(N,K)+1):
    # 右からj個
    for j in range(min(N-i, K-i)+1):
        tmp_score = 0
        pq = []
        for lef in range(i):
            if inl[lef] < 0:
                heapq.heappush(pq, inl[lef])
            tmp_score += inl[lef]
        for rg in range(j):
            if inl[N-1-rg] < 0:
                heapq.heappush(pq, inl[N-1-rg])
            tmp_score += inl[N-1-rg]
        for _ in range(K-i-j):
            if len(pq):
                minus = heapq.heappop(pq)
                tmp_score -= minus
        # print(pq)
        # print("i:{} j:{} nokori:{} tmp_score:{}".format(i,j,K-i-j, tmp_score))
        max_score = max(tmp_score, max_score)

print(max_score)
