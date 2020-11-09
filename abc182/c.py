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
    Ns = [int(c) for c in input()]

    res = 10**18
    for i in range(2**len(Ns)):
        cnt = 0
        cnt_erase = 0
        for k in range(len(Ns)):
            if 1 & (i >> k):
                cnt += Ns[k]
            else:
                cnt_erase += 1
        if cnt % 3 == 0:
            res = min(cnt_erase, res)

    if res == len(Ns):
        print(-1)
    else:
        print(res)

main()