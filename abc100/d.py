from itertools import product
N,M=map(int, input().split())
inl=[list(map(int, input().split())) for _ in range(N)]
res=0
for i,j,k in product(*[[1, -1]]*3):res=max(res,sum(sorted(map(lambda x: i*x[0]+j*x[1]+k*x[2], inl), reverse=True)[:M]))
print(res)
