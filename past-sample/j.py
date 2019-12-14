import sys
import heapq
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LIN(): return [-int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res

N,M=LI()

upper = 1 << N
DP=[1000000000000]*upper
DP[0] = 0
KS=[]
for i in range(M):
    a,b=LI()
    cover = 0
    for i in LI():
        cover |= (1 << (i-1))
    KS.append((a, cover))
# print(KS)

for i in range(M):
    cost, cover = KS[i]
    for j in range(upper):
        DP[j | cover] = min(DP[j | cover], DP[j] + cost)
if DP[upper-1] != 1000000000000:
    print(DP[upper-1])
else:
    print(-1)
