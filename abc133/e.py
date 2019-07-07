from collections import deque
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


N,K=LI()
mp = {}

if N == 1:
    print(K)
    exit()

for i in range(N-1):
    a,b = LI()
    if not a in mp: mp[a] = []
    if not b in mp: mp[b] = []
    mp[a].append(b)
    mp[b].append(a)

QU = deque([])
visited = set([1])

fact=[1]*(max(N,K)+1)
for i in range(1, max(N,K)+1):
    fact[i] = fact[i-1]*i%DVSR

def ncr(n,r):
    return fact[n]*INV(fact[r])*INV(fact[n-r])%DVSR

pat = ncr(K, len(mp[1])+1)*fact[len(mp[1])+1]%DVSR
for i in mp[1]:
    visited.add(i)
    QU.append(i)

while QU:
    vx = QU.popleft()
    nxcnt = len(mp[vx])
    if (nxcnt+1) > K:
        print(0)
        exit()
    notvisited = 0
    for nx in mp[vx]:
        if not nx in visited:
            QU.append(nx)
            visited.add(nx)
    pat = pat*fact[nxcnt-1]*ncr(K-2, nxcnt-1)%DVSR

print(pat)
