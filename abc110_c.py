import string
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

S=input()
T=input()

mp1={s: 0 for s in string.ascii_lowercase}
mp2={s: 0 for s in string.ascii_lowercase}
for i in range(len(S)):
    mp1[S[i]] += 1
    mp2[T[i]] += 1

li1 = list(mp1.values())
li2 = list(mp2.values())
li1.sort()
li2.sort()

print('Yes' if li1 == li2 else 'No')

