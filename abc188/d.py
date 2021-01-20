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
    for i in range(1, n+1):
        res.append(res[i-1]*i % DVSR)
    return res


def main():
    N, C = LI()
    HQ = []
    for _ in range(N):
        a, b, c = LI()
        heapq.heappush(HQ, (a, -1, c))
        heapq.heappush(HQ, (b+1, 1, c))

    res = 0
    price_sum = 0
    last = 0
    while HQ:
        r, sig, c = heapq.heappop(HQ)
        res += min(price_sum, C) * (r - last)
        price_sum -= sig*c
        last = r
    print(res)


if __name__ == "__main__":
    main()
