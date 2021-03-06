import sys
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

N,K=LI()
AS=LI()
lef = 0
rig = 0
sm = 0
cnt = 0
while lef <= rig:
    if sm >= K:
        cnt += (N-rig) + 1
        sm -= AS[lef]
        lef += 1
    else:
        if rig < N:
            sm += AS[rig]
            rig += 1
        else:
            # sm -= AS[lef]
            lef += 1
print(cnt)
