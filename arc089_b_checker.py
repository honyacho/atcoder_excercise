N,K=map(int, input().split())
K2=2*K
inmap=[[0]*K for _ in range(K2)]
accmap=[[0]*(K+1) for _ in range(K2+1)]
for i in range(N):
    line=input().split()
    x, y, wb=int(line[0]), int(line[1]), line[2]
    if wb == 'W':
        x += K
    y %= K2
    if y >= K:
        y=y%K
        x=(x+K)%K2
    else:
        x=x % K2
    inmap[x][y] += 1

for i in range(K2):
    for j in range(K):
        accmap[i+1][j+1]=inmap[i][j] + accmap[i+1][j] + accmap[i][j+1] - accmap[i][j]

res=0
for i in range(K):
    for j in range(K):
        cand=2*(accmap[i][j] - accmap[i+K][j]) + accmap[i+K][K] - accmap[i][K] + accmap[K2][j]
        res=max(res, cand, N-cand)

print(res)
