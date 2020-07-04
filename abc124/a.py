a,b=map(int, input().split())
res = 0
if a > b:
    res+=a
    a-=1
    if a>b:
        print(res+a)
    else:
        print(res+b)
else:
    res+=b
    b-=1
    if a>b:
        print(res+a)
    else:
        print(res+b)
