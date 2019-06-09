N=int(input())
inl = list(map(int,input().split()))

max_v = -100000000
max_i = -1
min_v = 100000000
min_i = -1
for i, num in enumerate(inl):
    if max_v < num: 
        max_v = num 
        max_i = i
    if min_v > num:
        min_v = num
        min_i = i

outl = []
if abs(min_v) > abs(max_v):
    for i in range(N):
        if inl[i] > min_v:
            inl[i] += min_v
            outl.append((min_i, i))
    for i in reversed(range(1, N)):
        if inl[i-1] > inl[i]:
            inl[i-1] += inl[i]
            outl.append((i, i-1))
else:
    for i in range(N):
        if inl[i] < max_v:
            inl[i] += max_v
            outl.append((max_i, i))
    for i in range(1, N):
        if inl[i-1] > inl[i]:
            inl[i] += inl[i-1]
            outl.append((i-1, i))

print(len(outl))
for i,j in outl: print(i+1, j+1)
