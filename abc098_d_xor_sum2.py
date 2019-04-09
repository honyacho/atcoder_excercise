num_inputs = int(input())
inputs = [int(st) for st in input().split()]
rnges = [(0,9)]
lf = 0
rg = 0
su = 0
score = 0
while rg < num_inputs:
    if su & inputs[rg] == 0:
        su += inputs[rg]
        if rnges[len(rnges)-1][0] == lf:
            rnges[len(rnges)-1] = (lf, rg+1)
        else:
            rnges.append((lf, rg+1))
        rg += 1
    else:
        su -= inputs[lf]
        lf += 1

tmp_rg = 0
for lf, rg in rnges:
    score += (rg-lf+1)*(rg-lf)//2
    if lf < tmp_rg:
        score -= ((tmp_rg-lf+1)*(tmp_rg-lf)//2)
    tmp_rg = rg

print(score)
