N=int(input())
inl= [] 
for i in range(N):
    name, score = input().split()
    score = -int(score)
    inl.append((name, score, i+1))

inl.sort()

for name, score, i in inl:
    print(i)
