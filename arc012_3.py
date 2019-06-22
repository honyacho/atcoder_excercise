board = [input() for i in range(19)]
white_cnt = 0
black_cnt = 0
for i in range(19):
    for j in range(19):
        if board[i][j] == 'x':
            white_cnt += 1
        if board[i][j] == 'o':
            black_cnt += 1


global ren_cnt
ren_cnt = {'x':[0]*10,'o':[0]*10}
def hantei(ren, prev):
    global ren_cnt
    if ren > 9:
        print('NO')
        exit()
    elif ren >= 5:
        ren_cnt[prev][ren] += 1

def judge(ren, prev, i, j):
    if i >= 0 and i < 19 and j >= 0 and j < 19:
        if prev == board[i][j] and prev != '.':
            ren += 1
        else:
            ren = 1
        hantei(ren, board[i][j])
        return ren, board[i][j]
    else:
        return 1, '.'

for i in range(19):
    ren = 1
    prev = '.'
    for j in range(19):
        ren, prev = judge(ren, prev, i, j)

for j in range(19):
    ren = 1
    prev = '.'
    for i in range(19):
        ren, prev = judge(ren, prev, i, j)

for k in range(-18, 19):
    ren = 1
    prev = '.'
    for l in range(19):
        i = k + l
        j = l
        ren, prev = judge(ren, prev,i,j)

for k in range(0, 37):
    ren = 1
    prev = '.'
    for l in range(19):
        i = k - l
        j = l
        ren, prev = judge(ren, prev,i,j)

# print(ren_cnt)
for i in range(5, 10):
    if ren_cnt['x'][i] > 1 or ren_cnt['o'][i] > 1:
        print('NO')
        exit()

white_win = ren_cnt['x'][5] > 0
black_win = ren_cnt['o'][5] > 0

if (white_win and black_cnt == white_cnt and not black_win) or \
    (black_win and not white_win and black_cnt == white_cnt+1) or \
    (not black_win and not white_win and (black_cnt == white_cnt+1 or black_cnt == white_cnt)):
    print('YES')
else:
    print('NO')