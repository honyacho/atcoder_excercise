import sys
import math
import itertools
import heapq
from collections import deque

sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 998244353
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

def main():
    N, K = LI ()
    DP = [0]*N
    DPS = [0]*(N+1)
    DP[0] = 1
    DPS[1] = 1
    LRS = [tuple(LI()) for i in range(K)]

    for i in range(N):
        for L, R in LRS:
            DP[i] += DPS[max(i-L+1, 0)] - DPS[max(i-R, 0)]
            DP[i] %= DVSR
        DPS[i+1] = DPS[i] + DP[i]
        DPS[i+1] %= DVSR

    # print(DP)
    print(DP[N-1])

main()