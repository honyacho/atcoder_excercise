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

digit_mod13 = 1
pats = [0]*13
buf = [0]*13

pats[0] = 1
N = len(S)
for i in range(N):
    if S[N-1-i] == '?':
        for k in range(10):
            zurasu = (k*digit_mod13) % 13
            # print(k*digit_mod13, zurasu)
            for j in range(13):
                buf[(j+zurasu)%13] += pats[j]
        for j in range(13):
            pats[j] = buf[j] % DVSR
        # flush
        for j in range(13):
            buf[j] = 0
    else:
        zurasu = (int(S[N-1-i])*digit_mod13) % 13
        for j in range(13):
            buf[(j+zurasu)%13] += pats[j]
        for j in range(13):
            pats[j] = buf[j]
        # flush
        for j in range(13):
            buf[j] = 0

    digit_mod13 = (digit_mod13*10) % 13

# print(pats)
# print(buf)

print(pats[5])
