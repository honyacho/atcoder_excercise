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
def II(): return int(sys.stdin.readline())
def SI(): return input()


s = input().replace('BC', 'D')

cnt = 0
res = 0
for i in range(len(s)):
    if s[i] == 'A':
        cnt += 1
    elif s[i] == 'D':
        res += cnt
    else:
        cnt = 0
print(res)
