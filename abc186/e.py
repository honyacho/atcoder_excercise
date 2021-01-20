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


def gcd(x, y):
    if x < y:
        x = x ^ y
        y = x ^ y
        x = x ^ y
    div = x % y
    while div:
        x = y
        y = div
        div = x % y
    return y


def eGCD(a: int, b: int) -> (int, int, int):
    if b == 0:
        return a, 1, 0
    d, y, x = eGCD(b, a % b)
    y -= a//b * x
    return d, x, y


def solve(n, start, k):
    gcd_nk = gcd(n, k)
    if start % gcd_nk != 0:
        return -1
    n //= gcd_nk
    start //= gcd_nk
    k //= gcd_nk
    pow(k, n-2, n)


def main():
    T = II()
    for i in range(T):
        N, S, K = LI()
        print(solve(N, S, K))


main()
