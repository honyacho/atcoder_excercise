N,K=map(int,input().split())
s=0
for b in range(K+1,N+1):s+=(N//b)*(b-K)+max(0,N%b-K+1)
print(s if K!=0 else N*N)
