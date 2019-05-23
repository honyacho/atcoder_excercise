M,K=map(int,input().split())

lis=[]
if K == 0:
    for i in range(2**M):
        lis.append(str(i))
        lis.append(str(i))
    print(" ".join(lis))
else:
    print("-1")
