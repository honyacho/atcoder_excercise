N,M=map(int, input().split())

cum=[0]*(N+1)
div_to_cnt={}
for i, n in enumerate(map(int, input().split()), start=1):
    cum[i] = cum[i-1] + n
    div = cum[i] % M
    if not div in div_to_cnt: div_to_cnt[div] = 0
    div_to_cnt[div] += 1

res = 0
for k,v in div_to_cnt.items():
    if k == 0: res += v
    res += v*(v-1) // 2
print(res)
