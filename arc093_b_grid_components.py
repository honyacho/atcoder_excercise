A,B=map(int,input().split())
print(100, 100)
resmap = [['.']*100 for _ in range(100)]

for i in range(A-1):
    from_btm = (i // 50)*2
    from_lft = (i % 50)*2
    resmap[99-from_btm][from_lft] = "."
    resmap[99-from_btm][from_lft+1] = "#"
    resmap[99-from_btm-1][from_lft] = "#"
    resmap[99-from_btm-1][from_lft+1] = "#"

for i in range(B-1+(A==1)):
    from_top = (i // 50)*2
    from_lft = (i % 50)*2
    resmap[from_top][from_lft] = "#"


for line in resmap:
    print(*line, sep="")
