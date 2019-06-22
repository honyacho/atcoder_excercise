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

N,K=LI()
INL=LI()

left=0
right=1
acc=INL[left]
res = 0
while left < N:
    if acc < K and right < N:
        acc+=INL[right]
        right+=1
    else:
        # print(left, right)
        if acc >= K:
            res += (N-(right-1))
        acc -= INL[left]
        left += 1

print(res)
