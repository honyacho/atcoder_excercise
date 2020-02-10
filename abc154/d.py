import sys
import math
from itertools import accumulate
import heapq
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

N,K=LI()
acc = LI()
for i in range(N):
    acc[i] = (1+acc[i]) / 2
acc2 = list(accumulate(acc))
# print(acc)
# print(acc2)

res = acc2[N-1] if K == N else 0
for i in range(1, N-K+1):
    if i == 1:
        res = acc2[K-1]
    else:
        res = max(res, acc2[i+K-1] - acc2[i-1])
    # print(i-1, i+K-1)

print(res)
