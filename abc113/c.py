N,M=map(int,input().split())

mp = {}
for i in range(M):
    P,Y=map(int,input().split())
    if not P in mp:
        mp[P] = []
    mp[P].append((Y,i))

res = ['']*M
for k, li in sorted(mp.items()):
    for i, (y, l) in enumerate(sorted(li)):
        res[l] = '{:06d}{:06d}'.format(k, i+1)

for st in res: print(st)
