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


N = II()
S = input()
allR = 0
for c in S:
    allR += c == 'R'

if allR == 0 or allR == N:
    print(0)
else:
    idx = S.find("R")
    if idx <= allR-1:
        print(allR-1)
    else:
        print(allR)
