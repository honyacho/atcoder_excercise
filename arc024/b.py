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


def getM(b):
    mx = 0
    cur = -1
    cnt = 0
    for v in b:
        if v != cur:
            cur = v
            cnt = 0
        cnt += 1
        mx = max(mx, cnt)
    return mx


def main():
    N = II()
    BUF = [0]*(N*2)
    for i in range(N):
        v = II()
        BUF[i] = v
        BUF[i+N] = v
    mx = getM(BUF)
    if mx != 2*N:
        mx -= 2
        print(mx//2 + (mx % 2) + 1)
    else:
        print(-1)


if __name__ == '__main__':
    main()
