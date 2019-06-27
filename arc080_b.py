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

H,W=LI()
N=II()
INL=LI()

row = [0]*W
items = list(enumerate(INL, 1))
# print(items)
cur = 0
cnt = 0
for i in range(H):
    rn = range(W) if i%2 == 0 else reversed(range(W))
    for j in rn:
        row[j] = items[cur][0]
        cnt += 1
        # print("{} cur {} cnt:{}".format(items[cur][0], cur,cnt))
        if cnt >= items[cur][1]:
            cnt = 0
            cur += 1
    print(*row)
