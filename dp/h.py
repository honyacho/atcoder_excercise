from collections import deque
DVSR = 1000000007
def LI(): return [int(x) for x in input().split()]
H,W=LI()
MP=[input() for _ in range(H)]
MEMO=[[(-1,0)]*W for _ in range(H)]
MEMO[0][0] = (0,1)
QU=deque([])

QU.append((0,0,0))
IT=[(1,0),(0,1)]
while QU:
    i,j,cost = QU.popleft()
    cost+=1
    pat = MEMO[i][j][1]
    for dy, dx in IT:
        ny, nx = i+dy, j+dx
        if ny < H and nx < W and MP[ny][nx] == '.':
            cost2, pat2 = MEMO[ny][nx]
            if cost2 == -1:
                MEMO[ny][nx] = (cost, pat)
                QU.append((ny,nx,cost))
            elif cost2 == cost:
                _pat = (pat+pat2)%DVSR
                MEMO[ny][nx] = (cost,_pat)

print(MEMO[H-1][W-1][1])