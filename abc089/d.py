H,W,D=map(int,input().split())

remmap = {}
for v, i, j in sorted(sum([[(v, i, j) for j, v in enumerate(map(int, input().split()))] for i in range(H)], [])):
    rem = v%D
    if not rem in remmap:
        remmap[rem] = [(v,i,j)]
    else:
        remmap[rem].append((v,i,j))

accmap = {}
for rem, lis in remmap.items():
    for i in range(len(lis)):
        if i == 0:
            accmap[rem] = (lis[0][0], [0])
        else:
            fv, l = accmap[rem]
            l.append(l[i-1] + abs(lis[i][1]-lis[i-1][1])+abs(lis[i][2]-lis[i-1][2]))

for i in range(int(input())):
    L,R=map(int,input().split())
    rem=L%D
    fv, lis = accmap[rem]
    print(lis[(R-fv)//D]-lis[(L-fv)//D])
