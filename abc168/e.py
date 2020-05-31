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

def gcd(x, y):
    if x < y:
        x = x ^ y
        y = x ^ y
        x = x ^ y
    div = x % y
    while div != 0:
        x = y
        y = div
        div = x % y
    return y


N=II()
MP1={}
A0 = 0
B0 = 0
AB0 = 0
RES=1
for i in range(N):
    A, B = LI()
    if A*B != 0:
        G = gcd(abs(A),abs(B))
        A //= G
        B //= G
        v = (abs(A), abs(B), A*B > 0)
        if not v in MP1:
            MP1[v] = 1
        else:
            MP1[v] += 1

    if A == 0 and B != 0: A0 += 1
    if A != 0 and B == 0: B0 += 1
    if A == 0 and B == 0: AB0 += 1

# print(MP1)

VIS = set()
for (vv, n) in MP1.items():
    (A, B, isPos) = vv
    v = (B, A, not isPos)
    if not v in VIS and not vv in VIS:
        VIS.add(v)
        VIS.add(vv)
        if v in MP1:
            m = MP1[v]
            RES = (RES*POW(2, n))%DVSR + (RES*POW(2, m))%DVSR - RES
            RES %= DVSR
        else:
            RES *= POW(2, n)
            RES %= DVSR

if A0 and B0:
    RES = (RES*POW(2, A0))%DVSR + (RES*POW(2, B0))%DVSR - RES
elif A0:
    RES = RES*POW(2, A0)%DVSR
elif B0:
    RES = RES*POW(2, B0)%DVSR


print((RES+AB0-1)%DVSR)
