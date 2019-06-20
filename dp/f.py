S=input()
T=input()
memo = [[0]*(len(T)+1) for _ in range(len(S)+1)]

for i in range(1, len(S)+1):
    for j in range(1, len(T)+1):
        if S[i-1] == T[j-1]:
            memo[i][j] = memo[i-1][j-1] + 1
        else:
            memo[i][j] = max(memo[i-1][j], memo[i][j-1])
 
ans = ''
i = len(S)
j = len(T)
while i > 0 and j > 0:
    if memo[i][j] == memo[i-1][j]:
        i-=1
    elif memo[i][j] == memo[i][j-1]:
        j-=1
    else:
        i-=1
        j-=1
        ans = ans + S[i]

ans = ''.join(reversed(ans))
print(ans)