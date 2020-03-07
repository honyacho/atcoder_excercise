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

K=II()
X,Y=LI()

if K%2 == 0 and (X+Y)%2 == 1:
    print(-1)
    exit()

if K == 1:
    print(abs(X)+abs(Y))
    coefx = -1 if X < 0 else 1
    coefy = -1 if Y < 0 else 1
    for i in range(1, abs(X)+1):
        print(coefx*i, 0)
    for i in range(1, abs(Y)+1):
        print(X, coefy*i)
else:
    res = []
    rest = (abs(X)+abs(Y)) % K if abs(X)+abs(Y) > K else (K - (abs(X)+abs(Y)) % K)
    rest %= K
    a = 0
    b = 0
    while rest:
        a = (rest+K)//2
        b = K-a
        rest -= abs(a-b)
        a *= (1 if abs(X)+abs(Y) > K else -1)*(1 if X >= 0 else -1)
        b *= -(1 if Y >= 0 else -1)
        # print("rest", rest)
        res.append((a, b))

    while a != X or b != Y:
        mov_rest = K
        distx = min(X-a, mov_rest) if X-a > 0 else max(X-a, -mov_rest)
        mov_rest -= abs(distx)

        disty = min(Y-b, mov_rest) if Y-b > 0 else max(Y-b, -mov_rest)
        # print("dist", distx, disty)

        a += distx
        b += disty
        res.append((a, b))
    print(len(res))
    for a, b in res:
        print(a, b)
