from bisect import bisect_left
N=int(input())
inp=[int(i)for i in input().split()]
inp.sort()
ma=inp[-1]
idx = bisect_left(inp[0:-1], ma//2)
if idx >= len(inp)-1:
    if idx >= len(inp)-1:
        print(ma, inp[idx-1])
    else:
        print(ma, inp[idx])
elif abs(inp[idx] - ma//2) < abs(ma//2 - inp[idx - 1]) or abs(ma - inp[idx] - ma//2) < abs(ma//2 - inp[idx - 1]):
    print(ma, inp[idx])
else:
    print(ma, inp[idx-1])
