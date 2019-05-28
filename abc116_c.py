N=int(input())
Hs=[0] + list(map(int,input().split()))
Hs.append(0)
ma = max(Hs)

res = 0
for _ in range(ma):
    cnt = 0
    last1 = -1
    for i in range(N+2):
        if Hs[i] > 0:
            Hs[i] -= 1
            if last1+1 != i:
                cnt += 1
            last1 = i
    res += cnt

print(res)
