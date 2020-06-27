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
def LI(): return [int(x) for x in sys.stdin.readline().split()]
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

N=II()

MP={}
for i in LI():
    if not i in MP: MP[i] = 0
    MP[i] += 1

Q=II()

res = 0
for i, j in MP.items():
    res += i*j

arr = []
for _ in range(Q):
    B, C = LI()
    if not B in MP: MP[B] = 0
    if not C in MP: MP[C] = 0
    diff = MP[B]*C - MP[B]*B
    MP[C] += MP[B]
    MP[B] = 0
    res += diff
    arr.append(res)

for i in arr: print(i)
