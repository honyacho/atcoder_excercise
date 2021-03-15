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


def main():
    N, M, Q = LI()

    INL = []
    for i in range(N):
        INL.append(tuple(LI()))

    XS = LI()

    BUF = []
    for i in range(Q):
        L, R = LI()
        L -= 1
        R -= 1
        INL2 = INL.copy()

        for i in range(M):
            if i < L or i > R:
                BUF.append(XS[i])
        BUF.sort()

        res = 0
        for b in BUF:
            MM = 0
            Mi = -1
            for i in range(N):
                w, v = INL2[i]
                if w != -1 and w <= b and MM < v:
                    MM = v
                    Mi = i
            if Mi != -1:
                INL2[Mi] = (-1, 0)
                res += MM

        print(res)
        BUF.clear()


if __name__ == '__main__':
    main()