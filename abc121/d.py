A, B = [int(i) for i in input().split(' ')]

count = B - A + 1

res = 0
ones = (count - (count % 2)) / 2
if count % 2:
    seed = A if A % 2 else B
    res = seed ^ (1 if ones % 2 else 0)
else:
    res = ((A % 2)*(A ^ B ^ 1)) ^ (1 if ones % 2 else 0)

print(res)
