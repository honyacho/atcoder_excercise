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

N=II()
lis = [[0]*10 for i in range(N)]
for i in range(N):
    cnt = 0
    for c in input():
        lis[i][cnt] = ord(c)
        cnt += 1
    lis[i].sort()
lis.sort()
# print(lis)

cur = [0]*10
cnt = 1
res = 0
for arr in lis:
    if arr == cur:
        cnt += 1
    else:
        res += (cnt*(cnt-1)//2)
        cur = arr
        cnt = 1
res += (cnt*(cnt-1)//2)

print(res)
