queue=[]
N,M=map(int,input().split())
NE=9223372036854775807
mp=[NE]*(N+1)
lst=[[] for _ in range(N+1)]
for _ in range(M):
    L,R,D = map(int, input().split())
    lst[L].append((L,R,D))
    lst[R].append((L,R,D))

def check(L, R, D):
    if mp[L] == NE:
        mp[L] = mp[R]-D
    elif mp[R] == NE:
        mp[R] = mp[L]+D
    else:
        if mp[L]+D != mp[R]:
            print("No")
            exit()

def check_list(ls, checking):
    while len(ls):
        L,R,D = ls.pop()
        check(L,R,D)
        nx = R if L == checking else L
        if len(lst[nx]): queue.append(nx)

for i in range(1, N+1):
    if mp[i] == NE: mp[i] = 0
    check_list(lst[i], i)

    while(len(queue) > 0):
        num = queue.pop()
        check_list(lst[num], num)
print("Yes")
