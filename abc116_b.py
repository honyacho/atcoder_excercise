s=int(input())
v_to_i = {}
cnt = 1
while not s in v_to_i:
    v_to_i[s] = cnt
    s = (s//2) if s&1 == 0 else (s*3+1)
    cnt += 1

print(cnt)
