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
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

def gcd(x, y):
    if x < y: x, y = y, x
    div = x % y
    while div != 0:
        x, y = y, div
        div = x % y
    return y

def main():
    N = II()
    XYS = [LI() for _ in range(N)]
    ST = set()
    STx = set()
    for p1, p2 in itertools.combinations(XYS, 2):
        dx = p2[0] - p1[0]
        dy = p2[1] - p1[1]
        bu = p1[1]*dx - p1[0]*dy
        bl = dx
        if dx:
            if dy:
                gcd1 = gcd(abs(dy), abs(dx))
                dy //= gcd1
                dx //= gcd1
            else:
                dy = 0
                dx = 0

            if bu:
                gcd2 = gcd(abs(bu), abs(bl))
                bu //= gcd2
                bl //= gcd2
            else:
                bu = 0
                bl = 0

            cand = (dy, dx, bu, bl)
            if cand in ST:
                print("Yes")
                exit()
            else:
                ST.add(cand)
        else:
            if p1[0] in STx:
                print("Yes")
                exit()
            else:
                STx.add(p1[0])

    print("No")

main()