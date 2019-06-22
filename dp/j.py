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
INL=LI()
INVN=1.0/N
INVN_1 = 1-INVN

DP=[[1,0,0,0] for _ in range(N+1)]

res = 0
for cnt in range(1, 100*N):

    for i in range(N):
        for j in reversed(range(1,3)):
            DP[i][j] = (DP[i][j-1] - DP[i][j])*INVN + DP[i][j]
        DP[i][0] = DP[i-1][0]*INVN_1

