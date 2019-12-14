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

N,M=LI()
INL=[tuple(LI()) for i in range(M)]
mp={}
fmt = "{:06d}{:06d}"
cur_p = 0
cur_cnt = 1
for i, (p, y) in enumerate(sorted(INL)):
    if cur_p != p:
        cur_cnt = 1
        cur_p = p
    mp[(p,y)] = fmt.format(p, cur_cnt)
    cur_cnt += 1

for tp in INL:
    print(mp[tp])
