import sys
import math
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

H,W=LI()

RS=[LI() for _ in range(H)]
BS=[LI() for _ in range(H)]
DS=[[False]*W for _ in range(H)]

siz = True
for i in range(H):
    for j in range(W):
        DS[i][j] = abs(RS[i][j] - BS[i][j])
        siz = max(siz, DS[i][j])

siz = 81*(H+W+1)
MP = [[[0]*siz for _ in range(W)] for _ in range(H)]
MP[0][0][DS[0][0]] = 1

for i in range(H):
    for j in range(W):
        d = DS[i][j]
        for k in range(0, siz-d):
            if i > 0:
                MP[i][j][abs(k-d)] = MP[i][j][abs(k-d)] or MP[i-1][j][k]
                MP[i][j][abs(k+d)] = MP[i][j][abs(k+d)] or MP[i-1][j][k]
            if j > 0:
                MP[i][j][abs(k-d)] = MP[i][j][abs(k-d)] or MP[i][j-1][k]
                MP[i][j][abs(k+d)] = MP[i][j][abs(k+d)] or MP[i][j-1][k]

# print(MP[i][j][:100])
for i in range(siz):
    if MP[H-1][W-1][i]:
        print(i)
        exit()
