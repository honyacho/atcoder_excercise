# from itertools import permutations
# res = set()
# for li in permutations([0,0,1,1,2,2,3,3]):
#     st = set()
#     for i in range(4):
#         idx = li.index(i)
#         xor_rep = li[idx]
#         for j in range(idx+1, 8):
#             xor_rep ^= li[j]
#             if li[j] == i:
#                 st.add(xor_rep)
#                 break
#     if len(st) == 1:
#         sol = st.pop()
#         if sol == li[0] and li[1] == 0 and li[7] == 0 and li[2] < li[3]:
#             res.add(li)
# print(res)

M,K=map(int,input().split())
MX=2**(M)
if (M == 1 and K != 0) or K > MX-1:
    print(-1)
    exit()

if K == 0:
    for i in range(MX):
        print(i,i,end=' ')
    print('')
else:
    print(K,end=' ')
    for i in range(MX):
        if i != K:
            print(i, end=' ')
    print(K, end=' ')
    for i in reversed(range(MX)):
        if i != K:
            print(i, end=' ')
    print('')
