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


N = II()
ST = input()
ST = ST[::-1]

# NUM1 =
# NUM2 =
popcnt = 0

for i in range(N):
    popcnt += ST[i] == '1'

NUM1 = 0
NUM2 = 0
pop_1 = popcnt-1
pop_2 = popcnt+1
for i in range(N):
    if ST[i] == '1':
        if pop_1 > 0:
            NUM1 += pow(2, i, pop_1)
            NUM1 %= pop_1
        if pop_2 <= N:
            NUM2 += pow(2, i, pop_2)
            NUM2 %= pop_2

# print(pop_1, pop_2)
# print(NUM1, NUM2)

for i in range(N):
    cnt = 1
    i = N-i-1
    if ST[i] == '1':
        # print("A")
        if pop_1 != 0:
            value = NUM1 - pow(2, i, pop_1)
            value %= pop_1
            while value:
                value %= bin(value).count("1")
                cnt += 1
            print(cnt)
        else:
            print(0)
    else:
        # print("B")
        value = NUM2 + pow(2, i, pop_2)
        value %= pop_2
        while value:
            value %= bin(value).count("1")
            cnt += 1
        print(cnt)
