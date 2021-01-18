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

VER = 0
HOR = 1
DIAG = 2

def refresh(MP, DPS, i, j):
    pat = (DPS[i-1][j][VER] + DPS[i][j-1][HOR] + DPS[i-1][j-1][DIAG]) % DVSR
    if MP[i-1][j-1] != '#':
        DPS[i][j][VER] = (DPS[i-1][j][VER] + pat) % DVSR
        DPS[i][j][HOR] = (DPS[i][j-1][HOR] + pat) % DVSR
        DPS[i][j][DIAG] = (DPS[i-1][j-1][DIAG] + pat) % DVSR

def main():
    H, W = LI()
    MP = [input() for _ in range(H)]
    DPS = [[[0,0,0] for _ in range(W+1)] for _ in range(H+1)]
    DPS[1][1][0] = 1
    DPS[1][1][1] = 1
    DPS[1][1][2] = 1

    for j in range(2, W+1):
        refresh(MP, DPS, 1, j)

    for i in range(2, H+1):
        for j in range(1, W+1):
            refresh(MP, DPS, i, j)

    print((DPS[H][W][DIAG]-DPS[H-1][W-1][DIAG])%DVSR)

main()