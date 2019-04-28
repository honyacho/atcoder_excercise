i,j,k=map(int, input().split())
if i < j:
    print("Yes" if k <= j and k >= i else "No")
else:
    print("Yes" if j <= k and i >= k else "No")
