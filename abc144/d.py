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

a,b,x=LI()

FUL=a*a*b

if x >= FUL*0.5:
    rest = FUL-x
    # rest = a*a*h*0.5
    h = rest / a / a * 2
    print((math.atan(h/a) / (2*math.pi))*360)
else:
    h = x / a / b * 2
    res = 90 - (math.atan(h / b) / (2*math.pi) * 360)
    print(res)
