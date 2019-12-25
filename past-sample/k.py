import sys
sys.setrecursionlimit(10**7)
INTMAX = 9223372036854775807
INTMIN = -9223372036854775808
DVSR = 1000000007
def POW(x, y): return pow(x, y, DVSR)
def INV(x, m=DVSR): return pow(x, m - 2, m)
def DIV(x, y, m=DVSR): return (x * INV(y, m)) % m
def LI(): return [int(x) for x in input().split()]
def LF(): return [float(x) for x in input().split()]
def LS(): return input().split()
def II(): return int(input())
def FLIST(n):
    res = [1]
    for i in range(1, n+1): res.append(res[i-1]*i%DVSR)
    return res
def DBL(lis): 
    for l in lis: print(l)

S=input()
T=input()

len_s = len(S)
len_2s = len_s*2
memo = [[-1]*26 for i in range(len_2s)]

lst = S[-1]
for i in range(1, len_2s):
    s_idx = len_s - 1 - (i % len_s)
    memo_idx = len_2s - 1 - i
    for al in range(26):
        memo[memo_idx][al] = memo[memo_idx+1][al] + 1 if memo[memo_idx+1][al] != -1 else -1
    memo[memo_idx][ord(lst)-97] = 1
    lst = S[s_idx]
# DBL(memo)

idx = S.find(T[0])
res = idx + 1
if idx == -1:
    print(-1)
else:
    for c in T[1:]:
        v = memo[idx][ord(c)-97]
        if v == -1:
            print(v)
            exit()
        else:
            res += v
            idx = (idx + v) % len_s
    print(res)
