N=int(input())
A=list(map(int, input().split()))
B=list(map(int, input().split()))
C = []
for i in range(N):
    C.append(A[i]-B[i])

C.sort(reverse=True)

summed = 0
for i in C:
    if i > 0:
        summed += i
print(summed)
