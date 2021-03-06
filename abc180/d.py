import sys
import math
import itertools
import heapq
from collections import deque

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


def main():
    X, Y, A, B = LI()
    cnt = 0
    while X*A <= B and X*A < Y:
        cnt += 1
        X *= A


    if (Y - A*X) > 0:
        cnt = cnt + max((Y - X) // B - (not (Y - X) % B), 1 + (Y - A*X) // B - (not (Y - A*X) % B))
    else:
        cnt = cnt + ((Y - X) // B) - (not (Y - X) % B)

    print(cnt)
main()