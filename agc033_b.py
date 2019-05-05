H,W,N=map(int,input().split())
sr,sc=map(int,input().split())
S=input()
T=input()

Scount = {'L':[0],'R':[0],'U':[0],'D':[0]}
Tcount = {'L':[0],'R':[0],'U':[0],'D':[0]}

rev = {'L':'R','D':'U','U':'D','R':'L'}

for i in range(N):
    for c in 'LRUD':
        if S[i] == c:
            Scount[S[i]].append(Scount[c][-1]+1)
        else:
            Scount[c].append(Scount[c][-1])
    for c in 'LRUD':
        if T[i] == c:
            if c == 'L':
                Tcount[T[i]].append(min(Tcount[T[i]][-1]+1,  Scount['R'][i+1] + sc - 1))
            if c == 'R':
                Tcount[T[i]].append(min(Tcount[T[i]][-1]+1,  W + Scount['L'][i+1] - sc))
            if c == 'D':
                Tcount[T[i]].append(min(Tcount[T[i]][-1]+1,  H + Scount['U'][i+1] - sr))
            if c == 'U':
                Tcount[T[i]].append(min(Tcount[T[i]][-1]+1,  Scount['D'][i+1] + sr - 1))
        else:
            Tcount[c].append(Tcount[c][-1])
for i in range(1, N+1):
    if (sc - (Scount['L'][i] - Tcount['R'][i-1]) < 1) or \
        (sc + (Scount['R'][i] - Tcount['L'][i-1]) > W) or \
        (sr + (Scount['D'][i] - Tcount['U'][i-1]) > H) or \
        (sr - (Scount['U'][i] - Tcount['D'][i-1]) < 1):
        print("NO")
        exit(0)

print("YES")
