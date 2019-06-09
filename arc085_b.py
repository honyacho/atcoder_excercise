N,Z,W=map(int, input().split())
INL = list(map(int,input().split()))

if N == 1:
    print(abs(INL[0]-W))
else:
    print(max(abs(W-INL[-1]), abs(INL[-2]-INL[-1])))
