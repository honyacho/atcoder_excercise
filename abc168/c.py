import sys
import math

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
A,B,H,M=LI()

ta = -(float(H+(M/60))*math.pi/6.0) + (math.pi*0.5)
tb = -(float(M)*math.pi/30.0) + (math.pi*0.5)
Ax = A*math.cos(ta)
Ay = A*math.sin(ta)

Bx = B*math.cos(tb)
By = B*math.sin(tb)

print(math.sqrt((Ax-Bx)*(Ax-Bx) + (Ay-By)*(Ay-By)))
