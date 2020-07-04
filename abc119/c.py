N,A,B,C = map(int, input().split(' '))
ls = [int(input()) for i in range(N)]

def dfs(n, a = 0, b = 0, c = 0, mp = 0):
    if n == N:
        return abs(A-a) + abs(B-b) + abs(C-c) + mp if a > 0 and b > 0 and c > 0 else 9223372036854775807
    else:
        return min(
            dfs(n+1, a + ls[n], b, c, mp + (10 if a > 0 else 0)),
            dfs(n+1, a, b + ls[n], c, mp + (10 if b > 0 else 0)),
            dfs(n+1, a, b, c + ls[n], mp + (10 if c > 0 else 0)),
            dfs(n+1, a, b, c, mp),
        )

print(dfs(0))
