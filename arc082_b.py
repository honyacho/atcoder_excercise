N=int(input())
INL=list(map(int,input().split()))

swp = 0
for i in range(0, N-1):
    if i+1 == INL[i]:
        INL[i] = INL[i] ^ INL[i+1]
        INL[i+1] = INL[i] ^ INL[i+1]
        INL[i] = INL[i] ^ INL[i+1]
        swp += 1

if INL[N-1] == N:
    INL[N-1], INL[N-2] = INL[N-2], INL[N-1]
    swp += 1

print(swp)
