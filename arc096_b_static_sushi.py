N,C=map(int,input().split())
IA=[eval(input().replace(" ",","))for _ in range(N)]
MS=[(0,0)]*(N+1)
CS=[0]*(N+1)
RS=0
for i,[a,v] in enumerate(IA):
  CS[i+1]=CS[i]+v
  MS[i+1]=max(CS[i+1]-a,MS[i][0]),max(CS[i+1]-2*a,MS[i][1])
for i in range(N):
  ob=CS[N]-CS[i]
  RS=max(RS,ob+MS[i][0]-2*(C-IA[i][0]),ob+MS[i][1]-(C-IA[i][0]))
print(max(RS,MS[N][0],0))
