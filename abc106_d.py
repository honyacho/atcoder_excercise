from itertools import product
N,M,Q=map(int, input().split())
ma1=[[0]*501 for i in range(501)]
ma=[[0]*501 for i in range(501)]
inpath=[[int(j) for j in input().split()] for i in range(M)]
inQ=[[int(j) for j in input().split()] for i in range(Q)]

for i, j in inpath:
    ma1[i][j] += 1

for i, j in  product(range(1, 501), range(1, 501)):
    ma[i][j] = ma[i][j-1] + ma1[i][j]

for fr, to in inQ:
    cnt = 0
    for j in range(fr, to+1):
        cnt += (ma[j][to] - ma[j][j-1])
    print(cnt)
