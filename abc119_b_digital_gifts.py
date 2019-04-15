n=int(input())
print(sum(map(lambda x: float(x[0])*(1 if x[1] == 'JPY' else 380000.0), [input().split() for i in range(n)])))
