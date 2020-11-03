import sys
import math
import heapq
import bisect

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

def calc(eve_sum: list, odd_sum: list, i: int, HS: list) -> int:
    eve_lat = eve_sum[-1] - eve_sum[i+1]
    odd_lat = odd_sum[-1] - odd_sum[i+1]
    res = 0
    if i % 2:
        res = (odd_sum[i-1] - eve_sum[i-1]) + (eve_lat - odd_lat - HS[i-1])
    else:
        res = (odd_sum[i] - eve_sum[i]) + (eve_lat - odd_lat)
    # print("res:", res)
    return res

def main():
    N, M = LI()
    HS = LI()
    HS.sort()

    WS = LI()
    WS.sort()
    if N == 1:
        print(min(map(lambda x: abs(x-HS[0]), WS)))
        exit()

    odd_sum = [0]*(N+1)
    odd_sum[2] = HS[1]

    eve_sum = [0]*(N+1)
    eve_sum[1] = HS[0]

    for i in range(2, N, 2):
        eve_sum[i] = eve_sum[i-1]
        eve_sum[i+1] = eve_sum[i-1] + HS[i]
    for j in range(1, N, 2):
        odd_sum[j] = odd_sum[j-1]
        odd_sum[j+1] = odd_sum[j-1] + HS[j]
    odd_sum[-1] = odd_sum[-2]

    res = 10**18
    for w in WS:
        i = bisect.bisect_right(HS, w)
        if i < N:
            score = calc(eve_sum, odd_sum, i, HS) + abs(HS[i] - w)
            if res > score:
                res = score
        if i-1 >= 0:
            score = calc(eve_sum, odd_sum, i-1, HS) + abs(HS[i-1] - w)
            if res > score:
                res = score
    print(res)

main()