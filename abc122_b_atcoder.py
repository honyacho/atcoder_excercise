instr = input()
tmp = 0
ma = 0
for c in instr:
    if c == 'A' or c == 'C' or c == 'G' or c == 'T':
        tmp += 1
        ma = max(ma, tmp)
    else:
        tmp = 0

print(ma)
