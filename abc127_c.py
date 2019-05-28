N,M=map(int, input().split())

mi = -1
ma = 100000000000
for i in range(M):
    l,r = map(int, input().split())
    mi = max(l, mi)
    ma = min(ma, r)

if ma >= mi:
    print(ma-mi+1)
else:
    print(0)
