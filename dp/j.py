import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, d=DVSR): return pow(x, d - 2, d)
def DIV(x, y, d=DVSR): return (x * INV(y, d)) % d
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

N=II()
Nd = float(N)
N_inv = 1/N
INIT = {1:0,2:0,3:0}
for i in LI():
    INIT[i] += 1

DP=[[[-1.0]*(N+2) for i in range(N+2)] for j in range(N+2)]
def solve(i, j, k):
    if DP[i][j][k] >= 0: return DP[i][j][k]
    if i+j+k == 0: return 0.0
    res = 0.0
    if i > 0: res += solve(i-1, j, k) * i
    if j > 0: res += solve(i+1, j-1, k) * j
    if k > 0: res += solve(i, j+1, k-1) * k
    res += Nd
    res *= 1.0 / (i + j + k)
    DP[i][j][k] = res
    return res

print(solve(INIT[1],INIT[2],INIT[3]))
