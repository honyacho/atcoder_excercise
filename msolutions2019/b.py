# M=int(input())
# N,K=list(map(int,input().split()))
# inl = [int(input()) for i in range(N)]

s = input()
cnt = 0
for i in range(len(s)):
    if s[i] == 'x':
        cnt+=1


if cnt >= 8:
    print('NO')
else:
    print('YES')
