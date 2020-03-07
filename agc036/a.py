import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y) -> int: return pow(x, y, DVSR)
def INV(x, d=DVSR) -> int: return pow(x, d - 2, d)
def DIV(x, y, d=DVSR) -> int: return (x * INV(y, d)) % d
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())

S=II()
DV=10**9
A=DV
B=(DV-(S%DV)) if S%DV else 0
C=1
D=(S+B)//A
# print(A*D-B*C)
print('0 0 {} {} {} {}'.format(A,B,C,D))
