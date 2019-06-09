N,C=map(int, input().split())
inl = [tuple(map(int, input().split())) for i in range(N)]
inl.sort()

res = 0
st = [(0,0)]*30
for s,t,c in inl:
    nx = (t,c)
    cnt = 0
    for i, (t1, c1) in enumerate(st):
        if not (t1 == s and c == c1) and t1 >= s:
            st[i] = (t1,c1)
        else:
            st[i] = nx
            nx = (0, 0)

        if st[i][0] != 0:
            cnt += 1
    res = max(cnt, res)

print(res)
