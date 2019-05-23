N=int(input())

naiv=0
endsA=0
startsB=0
both=0

for i in range(N):
    s=input()
    naiv+=s.count('AB')
    if s[0] == 'B' and s[-1] == 'A':
        both += 1
    elif s[0] == 'B':
        startsB += 1
    elif s[-1] == 'A':
        endsA += 1

# print("endsA {}".format(endsA))
# print("startsB {}".format(startsB))
# print("both {}".format(both))
# print("naiv {}".format(naiv))

res=naiv

min3 = min(endsA, startsB, both)
if min3 > 0:
    res += min3*2
    endsA -= min3
    startsB -= min3
    both -= min3

min2 = min(endsA, startsB)
if min2 > 0:
    res += min2
else:
    lower = min(max(endsA, startsB), both)
    if endsA > 0:
        endsA -= lower
    else:
        startsB -= lower
    both -= lower

res += both
print(res)
