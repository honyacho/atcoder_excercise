N=int(input())
S=input()

cnt = 0
cnt_black = 0
should_change = 0

cnt_black_arr = [0] * (N+1)

for i in range(N):
    if S[i] == '#':
        cnt_black += 1
    cnt_black_arr[i+1] = cnt_black

res = cnt_black
for i in range(N):
    num_black = N-i
    right_white = N - cnt_black - (i - cnt_black_arr[i])
    res = min(res, cnt_black_arr[i] + right_white)

print(res)
