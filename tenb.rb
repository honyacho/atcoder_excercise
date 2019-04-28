N=int(input())
S= input()
K=int(input())

print(map(lambda s: '*' if s != S[K-1] else s, S))
