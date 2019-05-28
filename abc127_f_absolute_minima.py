class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = [0] * (n + 1)
 
    def sum(self, i):
        s = 0
        while i > 0:
            s += self.tree[i]
            i -= i & -i
        return s
 
    def add(self, i, x):
        while i <= self.size:
            self.tree[i] += x
            i += i & -i
    
    def reset(self):
        t = self.tree
        for i in range(len(t)):
            t[i] = 0

# bit = Bit(10)
# bit.add(1, 1)
# bit.add(1, 1)

# # bit.add(2, 2)
# # bit.add(3, 3)
# print(bit.sum(1))

N=int(input())
queries = [tuple(map(int, input().split())) for _ in range(N)]

numl = []
for q in queries:
    if q[0] == 1:
        numl.append(q[1])
numl.sort()
val_to_key = {}

for i,v in enumerate(numl):
    if not v in val_to_key:
        val_to_key[v] = i

# print(numl)
# print(val_to_key)

cum_b = 0
cum_a = 0
bit = Bit(200005)
bit2 = Bit(200005)
cnt = 0

def abs_sum(mid):
    loc_sum = bit.sum(1+mid)
    lft_cnt = bit2.sum(1+mid)
    lef_sum = numl[mid]*lft_cnt - loc_sum
    rig_sum = cum_a-loc_sum - numl[mid]*(cnt-lft_cnt)
    return lef_sum + rig_sum

def solve():
    left = 0
    right = len(numl)-1
    mid = (left+right) // 2
    while left < mid:
        diff = abs_sum(mid+1) - abs_sum(mid)
        print("1t:{} 2t:{}".format(abs_sum(mid),abs_sum(mid+1)))
        print("diff{}".format(diff))
        if diff < 0:
            left = mid
        else:
            right = mid
        mid = (left+right) // 2

    res1, res_val1 = numl[left], abs_sum(left)+cum_b
    if left < len(numl)-1:
        res2, res_val2 = numl[left+1], abs_sum(left+1)+cum_b

    print("1:{} {} 2:{} {}".format(res1, res_val1, res2, res_val2))
    if res_val2 < res_val1:
        return res2, res_val2
    else:
        return res1, res_val1

for qu in queries:
    if qu[0] ==  1:
        _, a, b = qu
        bit.add(1+val_to_key[a], a)
        bit2.add(1+val_to_key[a], 1)
        cnt += 1
        cum_b += b
        cum_a += a
    else:
        sol, val = solve()
        print("{} {}".format(sol, val))

# for i in range(len(numl)):
#     print("dbg- abs sum: num{} val{}".format(numl[i], abs_sum(i)))

# cum = 0
# lis = []
# for _ in range(N):
#     qu=list(map(int, input().split()))
#     if qu[0] == 1:
#         lis.append(qu[1])
#         cum += qu[2]
#     else:
