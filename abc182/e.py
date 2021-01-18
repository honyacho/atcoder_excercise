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
def LI(): return map(int, sys.stdin.readline().split())
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

BALL = 1
BLOCK = 2
ENLIGHTEN = -1
def main():
    H, W, N, M = LI()
    MP = [[0]*W for i in range(H)]
    # light ball
    for _ in range(N):
        i, j = LI()
        i -= 1
        j -= 1
        MP[i][j] = BALL
    # blocks
    for _ in range(M):
        i, j = LI()
        i -= 1
        j -= 1
        MP[i][j] = BLOCK


    for i in range(H):
        for j in range(W):
            if MP[i][j] == BALL:
                for k in range(i+1, H):
                    if MP[k][j] > 0: break
                    MP[k][j] = ENLIGHTEN
                for k in range(0, i)[::-1]:
                    if MP[k][j] > 0: break
                    MP[k][j] = ENLIGHTEN

                for l in range(j+1, W):
                    if MP[i][l] > 0: break
                    MP[i][l] = ENLIGHTEN
                for l in range(0, j)[::-1]:
                    if MP[i][l] > 0: break
                    MP[i][l] = ENLIGHTEN

    res = 0
    # for arr in MP:
    #     print(arr)
    for i in range(H):
        for j in range(W):
            res += (MP[i][j] == ENLIGHTEN or MP[i][j] == BALL)
    print(res)

main()