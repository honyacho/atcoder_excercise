import itertools
import math
import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
MOD = 1000000007
def POW(x, y): return pow(x, y, MOD)
def INV(x, m=MOD): return pow(x, m - 2, m)
def DIV(x, y, m=MOD): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

N=II()
lis=[LI() for i in range(N)]
nums = list(range(N))

su = 0.0
for perm in itertools.permutations(nums, N):
    for i in range(len(perm)-1):
        su += math.sqrt((lis[perm[i]][0]-lis[perm[i+1]][0])**2 + (lis[perm[i]][1]-lis[perm[i+1]][1])**2)

print(su / math.factorial(N))
