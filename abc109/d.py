get_ints = lambda: [int(st) for st in input().split()]
H,W=get_ints()
inp=[get_ints() for i in range(H)]

res = []
for i in range(H):
    if not i % 2:
        for j in range(W):
            if inp[i][j] % 2:
                if j + 1 < W:
                    # print(i+1, j+1, i+1, j+2)
                    res.append([i+1, j+1, i+1, j+2])
                    inp[i][j] -= 1
                    inp[i][j+1] += 1
                elif i + 1 < H:
                    res.append([i+1, j+1, i+2, j+1])
                    inp[i][j] -= 1
                    inp[i+1][j] += 1
                # print(inp)
    else:
        for j in reversed(range(W)):
            if inp[i][j] % 2:
                if j - 1 >= 0:
                    res.append([i+1, j+1, i+1, j])
                    inp[i][j] -= 1
                    inp[i][j-1] += 1
                elif i + 1 < H:
                    res.append([i+1, j+1, i+2, j+1])
                    inp[i][j] -= 1
                    inp[i+1][j] += 1
                # print(inp)

print(len(res))
for ar in res:
    print(*ar)
