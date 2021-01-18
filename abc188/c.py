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
    N = II()
    AS = LI()
    ORG = list(AS)
    while len(AS) > 2:
        NEW = []
        for i in range(len(AS)//2):
            NEW.append(max(AS[2*i], AS[2*i+1]))
        AS = NEW
    print(ORG.index(min(AS))+1)

if __name__ == '__main__':
    main()

