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

N=II()
MP={}
res = 0
for i, A in reversed(list(enumerate(LI(), start=1))):
    if (-A-i) in MP: res += MP[-A-i]
    if not A-i in MP: MP[A-i] = 0
    MP[A-i] += 1
print(res)
