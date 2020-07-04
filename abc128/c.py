N,M = map(int, input().split())

ls = []
st = { i+1 for i in range(N) }
for i in range(M):
    inl = list(map(int, input().split()))
    switches = inl[1:]
    ls.append(switches)

checker = list(map(int,input().split()))

res = [0]
def check(inpu = st, mp = {}, res_ = res):
    if len(inpu):
        val = inpu.pop()
        mp0 = mp.copy()
        mp0[val] = 0
        mp1 = mp.copy()
        mp1[val] = 1
        check(inpu.copy(), mp0)
        check(inpu.copy(), mp1)
    else:
        # print(mp)
        all_ = True
        for key, sws in enumerate(ls):
            summed = 0
            for sw in sws:
                summed += mp[sw]
            summed %= 2
            if summed != checker[key]:
                all_ = False
        if all_:
            res[0] += 1

check()
print(res[0])
