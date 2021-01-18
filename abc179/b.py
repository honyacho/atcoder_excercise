import sys
import math
import itertools
import heapq
from collections import deque

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


def main():
    N = II()
    INL = [False]*N
    for i in range(N):
        a, b = LI()
        INL[i] = a == b
    for i in range(N-2):
        if INL[i] and INL[i+1] and INL[i+2]: return "Yes"
    return "No"

print(main())
