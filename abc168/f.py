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

Ax = A*math.cos(-H*math.pi/6-(math.pi*0.5))
Bx = B*math.cos(-M*math.pi/30-(math.pi*0.5))
Ay = A*math.sin(-H*math.pi/6-(math.pi*0.5))
By = B*math.sin(-M*math.pi/30-(math.pi*0.5))

print(math.sqrt((Ax-Bx)*(Ax-Bx) + (Ay-By)*(Ay-By)))
