import sys
import math
import itertools
import heapq
from collections import deque
from numba import njit

sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return map(int, sys.stdin.readline().split())
def LF(): return map(float, sys.stdin.readline().split())
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

def dist(MP, i, j):
    return abs(MP[j][0]-MP[i][0]) + abs(MP[j][1]-MP[i][1]) + max(0, MP[j][2] - MP[i][2])

def main():
    N = II()
    MP = [list(LI()) for i in range(N)]
    DP = [[-1]*(2**N) for i in range(N)]
    for i in range(1, N):
        DP[i][1 << i] = abs(MP[0][0]-MP[i][0]) + abs(MP[0][1]-MP[i][1]) + max(0, MP[i][2] - MP[0][2])

    def dp(pos: int, state: int):
        if DP[pos][state] != -1: return DP[pos][state]

        res = 10**18
        for k in range(1, N):
            if k != pos and (1 << k) & state:
                res = min(res, dp(k, state - (1 << pos)) + dist(MP, k, pos))

        DP[pos][state] = res
        return res

    print(dp(0, (1 << N) - 1))

main()