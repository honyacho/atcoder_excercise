R,G,B,N=map(int,input().split())

res = 0
for i in range(0, N//R + 1):
    for j in range(0, (N-i*R)//G + 1):
        if (N-i*R-j*G)%B == 0:
            res+=1

print(res)
