import sys
import math
from collections import deque

sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

N,M=LI()
RES = [-1]*(N+1)
RES[N] = 0.0

MP=[[] for i in range(N+1)]
for _ in range(M):
    i, j = LI()
    MP[i].append(j)

for i in range(N-1, 0, -1):
    div = len(MP[i])
    next_E = 0
    for j in MP[i]: next_E += RES[j] + 1
    RES[i] = next_E / div

result = RES[1]
RESN = [0]*(N+1)

for i in range(1, N-1):
    if len(MP[i]) == 1: continue
    max_j = max((RES[w],w) for w in MP[i])[1]

    for k in range(N-1, 0, -1):
        div = len(MP[k])
        next_E = 0
        for j in MP[k]:
            if k != i or j != max_j:
                next_E += RESN[j]
            else:
                div -= 1
        RESN[k] = (next_E / div) + 1.0
    result = min(result, RESN[1])

print(result)
