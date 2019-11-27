import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
MOD = 1000000007
def POW(x, y): return pow(x, y, MOD)
def INV(x, m=MOD): return pow(x, m - 2, m)
def DIV(x, y, m=MOD): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

N,K=LI()
AS=LI()

DP=[[0*N] for _ in range(K+1)]

for i in range(0,N):
    for k in range(AS[i]):
        DP[i][k] += 1

    for k in range(AS[i]):
        DP[i][k] = DP[i-1][]
