S=input()
N=len(S)
res=N
for i in range(1,N):
    if S[i-1] != S[i]:
        res = min(res,max(i, N-i))
print(res)
