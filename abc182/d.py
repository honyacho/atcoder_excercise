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
    ACC = [0]*(N+1)
    ACC_M = [0]*(N+1)
    As = LI()
    for i in range(N):
        ACC[i+1] = ACC[i] + As[i]
    for i in range(N):
        ACC_M[i+1] = max(ACC[i+1], ACC_M[i])

    res = 0
    summ = 0
    for i in range(1, N+1):
        res = max(summ + ACC_M[i], res)
        summ += ACC[i]
        res = max(summ, res)

    print(res)

main()