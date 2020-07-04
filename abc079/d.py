H,W=map(int,input().split())

MAT=[list(map(int, input().split())) for i in range(10)]
INM=[list(map(int, input().split())) for i in range(H)]


for k in range(10):
    for i in range(10):
        for j in range(10):
            MAT[i][j] = min(MAT[i][j], MAT[i][k] + MAT[k][j])
            MAT[j][i] = min(MAT[j][i], MAT[j][k] + MAT[k][i])

res = 0
for i in range(H):
    for j in range(W):
        if INM[i][j] != -1:
            res += MAT[INM[i][j]][1]

print(res)
