import sys
import math
import heapq
from itertools import permutations
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


S = input()

if len(S) < 4:
    for s in permutations(S):
        # print("".join(s))
        if int("".join(s)) % 8 == 0:
            print("Yes")
            exit()
    print("No")
else:
    input_cnt = [0]*10
    for c in S:
        input_cnt[int(c)] += 1

    num_cnt = [0]*10
    for i in range(100, 1000):
        if i % 8 == 0:
            ss = str(i)
            for s in ss:
                num_cnt[int(s)] += 1

            res = True
            for i in range(10):
                res = res and input_cnt[i] >= num_cnt[i]
                # reset
                num_cnt[i] = 0

            if res:
                print("Yes")
                exit()
    print("No")