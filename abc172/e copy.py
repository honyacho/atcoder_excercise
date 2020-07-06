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
def LI(): return map(int, sys.stdin.readline().split())
def LF(): return [float(x) for x in sys.stdin.readline().split()]
def LS(): return sys.stdin.readline().split()
def II(): return int(sys.stdin.readline())


def FLIST(n):
    res = [1]
    for i in range(1, n+1):
        res.append(res[i-1]*i % DVSR)
    return res


class ModInt:
    def __init__(self, a, dvsr=DVSR):
        self.dvsr = dvsr
        self.value = a % dvsr

    def __iadd__(self, b):
        self.value += b
        self.value %= self.dvsr

    def __isub__(self, b):
        self.value -= b
        self.value %= self.dvsr

    def __imul__(self, b):
        self.value *= b
        self.value %= self.dvsr

    def __ifloordiv__(self, b):
        self.value *= pow(b, self.dvsr - 2, self.dvsr)
        self.value %= self.dvsr

    def __str__(self):
        return str(self.value)


N, M = LI()
FACT = FLIST(M)


def NCR(n, r):
    res = FACT[n-r]
    res *= FACT[r]
    res %= DVSR
    res = INV(res)
    res *= FACT[n]
    res %= DVSR
    return res


def NPR(n, r):
    res = FACT[n]*INV(FACT[n-r])
    res %= DVSR
    return res


ALL = ModInt(NPR(M, N), DVSR)
ALL *= ALL.value

PAT = ModInt(0)
for i in reversed(range(1, N+1)):
    v = ModInt(NCR(N, i), DVSR)
    v *= NPR(M, i)
    v *= NPR(M-i, N-i)
    v *= NPR(M-i, N-i)
    PAT = ModInt(v.value - PAT.value, DVSR)

print(ModInt(ALL.value - PAT.value, DVSR))
