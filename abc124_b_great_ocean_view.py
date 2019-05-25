n=int(input())
arr=list(map(int, input().split()))
ma=arr[0]
res=1
for h in arr[1:]:
    if h >= ma:
        res+=1
        ma = h

print(res)
