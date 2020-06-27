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

N=II()-1
crr=[chr(97 + i) for i in range(26)]

res = []
cnt = 0
for i in range(1, 15):
    if N >= 26**i:
        cnt = i
        # print(26**i)
        N -= 26**i

# print(N)
while N:
    res.append(crr[N%26])
    N //= 26
res.reverse()
# res.append(crr[N%26])

print(("a"*(cnt+1) + "".join(res))[-(cnt+1):])
