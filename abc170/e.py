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

class LazyMin:
    def __init__(self, coef):
        self.h_add = []
        self.h_del = []
        self.coef = coef

    def add(self, v):
        heapq.heappush(self.h_add, self.coef*v)

    def add_diff(self, v):
        bef = self.min()
        self.add(v)
        aft = self.min()
        return (bef, aft)

    def delete(self, v):
        heapq.heappush(self.h_del, self.coef*v)

    def delete_diff(self, v):
        bef = self.min()
        self.delete(v)
        aft = self.min()
        return (bef, aft)


    def min(self):
        while self.h_del and self.h_add[0] == self.h_del[0]:
            heapq.heappop(self.h_add)
            heapq.heappop(self.h_del)
        if not self.h_add:
            return 0
        else:
            return self.coef*self.h_add[0]

    def __str__(self):
        while self.h_del and self.h_add[0] == self.h_del[0]:
            heapq.heappop(self.h_add)
            heapq.heappop(self.h_del)
        return "{} {}".format(self.h_add, self.h_del)

N,Q=LI()
MP=[(0,0) for i in range(N+1)]
SC_TO_MAX={}
AL_MIN=LazyMin(1)

for i in range(1,N+1):
    A,B=LI()
    MP[i] = (A,B)
    if not B in SC_TO_MAX: SC_TO_MAX[B] = LazyMin(-1)
    SC_TO_MAX[B].add(A)

for k, v in SC_TO_MAX.items():
    AL_MIN.add(v.min())

for i in range(Q):
    C,D=LI()
    rate, you = MP[C]
    MP[C] = (rate, D)
    if not D in SC_TO_MAX: SC_TO_MAX[D] = LazyMin(-1)

    rate_bef, rate_aft = SC_TO_MAX[you].delete_diff(rate)

    if rate_bef != rate_aft:
        AL_MIN.delete(rate_bef)
        if rate_aft: AL_MIN.add(rate_aft)

    rate_bef, rate_aft = SC_TO_MAX[D].add_diff(rate)

    if rate_bef != rate_aft:
        if rate_bef: AL_MIN.delete(rate_bef)
        AL_MIN.add(rate_aft)

    print(AL_MIN.min())
