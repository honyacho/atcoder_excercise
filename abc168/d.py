import sys
import collections
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

DQ=collections.deque([(1,0)])
VS=set([1])
MP={}
N,M=LI()
RES=[0]*(N+1)

for i in range(M):
    ff,tt=LI()
    if not ff in MP: MP[ff] = []
    if not tt in MP: MP[tt] = []
    MP[ff].append(tt)
    MP[tt].append(ff)

# print("----")
while DQ:
    i, dist = DQ.popleft()
    # print(i,dist)
    if i in MP:
        for j in MP[i]:
            if not j in VS:
                VS.add(j)
                DQ.append((j, dist+1))
                RES[j] = i

# print(VS, MP)
if len(VS) < N:
    print("No")
else:
    print("Yes")
    for i in range(2, N+1):
        print(RES[i])
