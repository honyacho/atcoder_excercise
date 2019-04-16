inp = int(input())
sequ = []
se = 1

incp = inp
while incp:
    if incp > se:
        incp -= se
        sequ.append(se)
        se = se << 1
        # print(incp)
    else:
        break

res=[]
for i in range(len(sequ)):
    res.append([i+1, i+2, 0])
    res.append([i+1, i+2, sequ[i]])

sd = 2**len(sequ)
for i, elem in reversed(list(enumerate(sequ))):
    if 2**(i+1) + sd <= inp:
        res.append([i+2, len(sequ)+1, sd])
        sd += 2**(i+1)
if sd == inp - 1:
    res.append([1, len(sequ)+1, sd])

print(len(sequ)+1, len(res))
for r in res:
    print(*r)
