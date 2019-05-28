N,M=map(int, input().split())

lst = [0 for i in range(M+1)]
for i in range(N):
    for j in list(map(int, input().split()))[1:]:
        lst[j] += 1

cnt = 0
for i in range(1, M+1):
    if lst[i] == N:
        cnt += 1

print(cnt)
