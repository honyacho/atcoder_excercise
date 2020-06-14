import sys
import math
import heapq
import bisect
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

X,N=LI()
L=LI()
L.sort()

# print(L)

for i in range(1000):
    ip=bisect.bisect_left(L, X+i)
    im=bisect.bisect_left(L, X-i)
    # print(i)

    res = None
    if ip >= 0 and ip < N:
        if L[ip] != X+i:
            res = X+i
    else:
        res = X+i

    if im >= 0 and im < N:
        if L[im] != X-i:
            res = X-i
    else:
        res = X-i

    if res != None:
        print(res)
        exit()
