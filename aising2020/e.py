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
    for i in range(1, n+1):
        res.append(res[i-1]*i % DVSR)
    return res


T = II()

MP = {}
for _ in range(T):
    MP.clear()
    N = II()
    for i in range(N):
        K, L, R = LI()
        if not K in MP:
            MP[K] = []
        MP[K].append((L, R))

    cnt = 0
    rest = []
    for k in range(1, N+1):
        if k in MP:
