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

N,K=LI()

if K > (N-1)*(N-2)//2:
    print(-1)
    exit()

out = []
for i in range(N-1):
    out.append((1, 2+i))

cnt = 0
for i in range(2, N+1):
    for j in range(i+1, N+1):
        if cnt < ((N-1)*(N-2)//2-K):
            cnt += 1
            out.append((i, j))

print(len(out))
for li in out:
    print(li[0],li[1])
