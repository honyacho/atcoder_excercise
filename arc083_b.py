N=int(input())
MP=[list(map(int,input().split())) for i in range(N)]
MP2=[]
for li in MP:
    MP2.append([i for i in li])

MP3=[[-1]*N for _ in range(N)]

# ワーシャルフロイド
for k in range(N):
    for i in range(N):
        for j in range(N):
            cand = MP2[i][k] + MP2[k][j]
            if cand <= MP2[i][j]:
                MP2[i][j] = cand
                if (i != k and j != k):
                    MP3[i][j] = k

for i in range(N):
    for j in range(N):
        if MP[i][j] != MP2[i][j]:
            print(-1)
            exit()

checked=set()

res = set()
def dfs(i,j):
    k = MP3[i][j]
    if k == -1:
        k = i
    if (i,j) in checked:
        return
    checked.add((i,j))
    if (i == k or j == k):
        if i < j:
            res.add((i,j))
    else:
        dfs(i,k)
        dfs(k,j)

for i in range(N):
    for j in range(N):
        dfs(i,j)

ressum = 0
for i,j in res:
    ressum += MP[i][j]

# for li in MP3:
#     print(li)
# print(res)
print(ressum)
