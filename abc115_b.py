N=int(input())
# list(map(int,input().split()))
inl = [int(input()) for i in range(N)]
inl.sort()

print(sum(inl[:N-1])+inl[N-1]//2)
