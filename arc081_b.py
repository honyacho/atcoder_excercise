DIV=10**9+7
N=int(input())
ST=[input(), input()]
PST=[]
ptr=0
while ptr < N:
    # 1枚のとき
    if ST[0][ptr] == ST[1][ptr]:
        ptr += 1
        PST.append(0)
    # 2枚のとき
    else:
        ptr += 2
        PST.append(1)

# print(PST)

res = 3 if PST[0] == 0 else 6
for i in range(len(PST)-1):
    if PST[i] == 0 and PST[i+1] == 0:
        res = (res*2)%DIV
    elif PST[i] == 0 and PST[i+1] == 1:
        res = (res*2)%DIV
    elif PST[i] == 1 and PST[i+1] == 0:
        res = res
    elif PST[i] == 1 and PST[i+1] == 1:
        res = (res*3)%DIV

print(res)
