N,K=map(int, input().split())
instr=input()
lft=0
rgt=1
voids=int(instr[0] == '0')
maxlen=0
while lft < rgt:
    maxlen = max(maxlen, rgt-lft)
    print("lft {} rgt {} maxlen {} void {} {}".format(lft, rgt, maxlen, voids, instr[lft:rgt]))
    if rgt < N and (instr[rgt] == '1' or (instr[rgt-1] == '0' and instr[rgt] == '0')):
        rgt += 1
    elif rgt < N and voids < K:
        voids += 1
        rgt += 1
    else:
        voids -= lft+1 < N and instr[lft] == '0' and instr[lft+1] == '1'
        lft += 1
print(maxlen)
