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
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

hq = list(LI())
heapq.heapify(hq)

cnt = 0
while 1:
    if hq[1] == hq[0] and hq[0] == hq[2]:
        break
    else:
        i = heapq.heappop(hq)
        j = heapq.heappop(hq)
        if i == j:
            heapq.heappush(hq, i+1)
            heapq.heappush(hq, i+1)
        else:
            heapq.heappush(hq, i+2)
            heapq.heappush(hq, j)
        cnt += 1

print(cnt)
