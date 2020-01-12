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
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res
def gcd(x, y):
    if x < y: x, y = y, x
    div = x % y
    while div != 0:
        x, y = y, div
        div = x % y
    return y

N=II()
HS=LI()

if N == 1:
    print("Yes")
elif N == 2:
    print("Yes" if abs(HS[0] - HS[1]) <= 1 else "No")
else:
    for i in range(1, N)[::-1]:
        if HS[i] >= HS[i-1]:
            continue
        elif HS[i-1] - HS[i] == 1:
            HS[i-1] -= 1
        else:
            print("No")
            exit()
    print("Yes")
