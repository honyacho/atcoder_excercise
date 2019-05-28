R,D,X=map(int, input().split())

x = X
for i in range(10):
    x = x*R - D
    print(x)
