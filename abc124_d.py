N,K=map(int, input().split())
instr=input()
lft=0
rgt=1
voids=0 if instr[0] == '1' else 1

maxlen=0
while lft < rgt:
    maxlen = max(maxlen, rgt-lft)
    if rgt < N and (instr[rgt] == '1' or (instr[rgt-1] == '0' and instr[rgt] == '0')):
        rgt += 1
    elif rgt < N and instr[rgt] == '0' and voids < K:
        voids += 1
        rgt += 1
    else:
        if lft+1 < N and instr[lft] == '0' and instr[lft+1] == '1':
            voids -= 1
        lft += 1

print(maxlen)
