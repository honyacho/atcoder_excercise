import math
N=int(input())
rt = int(math.sqrt(N))
# print(rt)

res = 0
for a in range(1, rt+1):
    if N % a == 0:
        b1 = N // a
        b = b1-1 
        if b > a and b > 0:
            print(a, b)
            res += b

print(res)
