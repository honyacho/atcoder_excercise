import sys
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LIN(): return [-int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res


H,W=LI()
MP=[input() for i in range(H)]
# 横スコア
MPS1=[[0]*W for i in range(H)]
# 縦スコア
MPS2=[[0]*W for i in range(H)]

for i in range(H):
    cnt = 0
    for j in range(W):
        if MP[i][j] == ".":
            cnt += 1
        else:
            for d in range(cnt):
                MPS1[i][j-d-1] = cnt
            cnt = 0
    for d in range(cnt):
        MPS1[i][W-d-1] = cnt

for j in range(W):
    cnt = 0
    for i in range(H):
        if MP[i][j] == ".":
            cnt += 1
        else:
            for d in range(cnt):
                MPS2[i-d-1][j] = cnt
            cnt = 0
    for d in range(cnt):
        MPS2[H-d-1][j] = cnt
# print(MPS1)
# print(MPS2)
res = 0
for i in range(H):
    for j in range(W):
        res = max(res,MPS1[i][j]+MPS2[i][j]-1)
print(res)
