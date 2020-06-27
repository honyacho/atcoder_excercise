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

N,M,K = LI()
AS=LI()
BS=LI()
ASC=[0]*(N+1)
BSC=[0]*(M+1)

for i in range(N):
    ASC[i+1] = ASC[i] + AS[i]
for i in range(M):
    BSC[i+1] = BSC[i] + BS[i]

# print(ASC)
# print(BSC)

res = 0

for i in range(0, N+1):
    # Aを i冊
    rest = K-ASC[i]
    if rest >= 0:
        idx = bisect.bisect_right(BSC, rest)
        # print("rest:{}, idx: {}".format(rest, idx))
        res = max(res, i+idx-1)
print(res)
