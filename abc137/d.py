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
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
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

N,M=LI()

Ws=[]
for i in range(N):
    a,b=LI()
    Ws.append((a,b))
Ws.sort()

cur = 0
HQ=[]
res = 0

for rest in range(1,M+1):
    while cur < N and Ws[cur][0] <= rest:
        heapq.heappush(HQ, -Ws[cur][1])
        cur += 1

    if HQ:
        nagated_gain = heapq.heappop(HQ)
        # print("debug: {} {}".format(rest, -nagated_gain))
        res -= nagated_gain

print(res)
