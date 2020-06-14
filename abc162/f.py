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
AS=LI()
DP=[[0,0,-10**18,-10**18,-10**18,-10**18] for i in range(N+1)]

for i in range(N):
    # 使った場合(2つ空けなし)
    DP[i+1][0] = DP[i][1]+AS[i]
    # 使わなかった場合(2つ空けなし)
    DP[i+1][1] = DP[i][0]
    # 使った場合(2つ空けあり)
    DP[i+1][2] = DP[i][3]+AS[i]
    # 使わなかった場合(2つ空けあり)
    DP[i+1][3] = max(DP[i][2], DP[i][1])

if N%2 == 0:
    print(max(DP[N][0], DP[N][1]))
else:
    SML=sum(AS[::2])
    MX=-10**18
    for i in AS[::2]:
        MX=max(MX, SML-i)
    print(MX, SML)
    print(max(DP[N][1], DP[N][2], DP[N][3], MX))
