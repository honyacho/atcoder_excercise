import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
N=II()
AS=LI()
BS=LI()

sm = 0
for i in range(N):
    rest = BS[i]
    taosu = min(AS[i], rest)
    AS[i] -= taosu
    rest -= taosu
    sm += taosu

    taosu2 = min(AS[i+1], rest)
    AS[i+1] -= taosu2
    rest -= taosu2
    sm += taosu2

print(sm)
