from bisect import bisect
LONG_MIN = -9223372036854775808
LONG_MAX = 9223372036854775807

num_a,num_b,num_q = map(int, input().split(' '))
lsa = [int(input()) for _ in range(num_a)] + [LONG_MIN, LONG_MAX]
lsb = [int(input()) for _ in range(num_b)] + [LONG_MIN, LONG_MAX]
lsa.sort()
lsb.sort()
lsq = [int(input()) for _ in range(num_q)]

for ques in lsq:
    lower_bound_a = bisect(lsa, ques)
    lower_bound_b = bisect(lsb, ques)
    upper_bound_a = lower_bound_a - 1
    upper_bound_b = lower_bound_b - 1

    res = min(
        max(lsa[lower_bound_a], lsb[lower_bound_b]) - ques, 
        ques - min(lsa[upper_bound_a], lsb[upper_bound_b]),
        lsb[lower_bound_b] - ques + lsb[lower_bound_b] - lsa[upper_bound_a],
        ques - lsa[upper_bound_a] + lsb[lower_bound_b] - lsa[upper_bound_a],
        lsa[lower_bound_a] - ques + lsa[lower_bound_a] - lsb[upper_bound_b],
        ques - lsb[upper_bound_b] + lsa[lower_bound_a] - lsb[upper_bound_b],
    )
    
    print(res)
