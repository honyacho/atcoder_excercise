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
GA,SA,BA=LI()
GB,SB,BB=LI()

GM,SM,BM = max(GA,GB), max(SA,SB), max(BA,BB)
Gm,Sm,Bm = min(GA,GB), min(SA,SB), min(BA,BB)

res = N
for i in range(N+1):
    num_g = i//Gm
    rest_g = i % Gm
    for j in range(0, N-i+1):
        k = N-j-i

        num_s = j//Sm
        rest_s = j % Sm

        num_b = k // Bm
        rest_b = k % Bm

        print('i:{},j:{},k:{} res:{}'.format(i,j,k, rest_g + rest_s + rest_b + num_g*GM + num_s*SM + num_b*BM))
        res = max(res, rest_g + rest_s + rest_b + num_g*GM + num_s*SM + num_b*BM)

print(res)
