N,M=map(int, input().split())
inlist = [tuple([int(st) for st in input().split()]) for i in range(M)]
inlist.sort()
res=0
minright=100000000000
for fr, to in inlist:
    if to < minright: minright = to
    if minright <= fr:
        res += 1
        minright = to
print(res+1)
