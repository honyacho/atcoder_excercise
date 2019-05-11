N,H=map(int,input().split())
A=[0]*N
B=[0]*N
for i in range(N):
 a,b=map(int,input().split())
 A[i]=a
 B[i]=b
A.sort(reverse=True)
B.sort(reverse=True)

cnt=0
for b in B:
 if A[0] < b:
  H-=b
  cnt+=1
 else:break
 if H<=0:break
print(cnt+((H//A[0])+(H%A[0]!=0)if H>0 else 0))
