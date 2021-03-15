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
    A, B, W = LI()
    A = float(A)
    B = float(B)
    W = W*1000.0

    min_ans = 10**18
    max_ans = -1
    for i in range(1, 1000001):
        res = W / i
        if res >= A and res <= B:
            min_ans = min(i, min_ans)
            max_ans = max(i, max_ans)

    if max_ans != -1:
        print(min_ans, max_ans)
    else:
        print("UNSATISFIABLE")

if __name__ == '__main__':
    main()