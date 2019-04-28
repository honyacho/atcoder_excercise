from functools import reduce
N=int(input())
NS=[int(i) for i in input().split()]
Nminus = 0
Nzero = 0
minabs = 9223372036854775807
abssum = 0
for i in NS:
    if i < 0:
        Nminus += 1
    elif i == 0:
        Nzero += 1
    minabs = min(abs(i), minabs)
    abssum += abs(i)

if Nminus % 2 == 0 or Nzero > 0:
    print(abssum)
else:
    print(abssum - 2*minabs)
