N=int(input())
inl = list(map(int,input().split()))
inl.sort(reverse=True)

if inl[0] < sum(inl[1:]):
    print("Yes")
else:
    print("No")
