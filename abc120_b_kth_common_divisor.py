a, b, k = map(lambda x: int(x), input().split(' '))

def gcd(a, b):
  cand = a % b
  if cand == 0:
    return b
  else:
    return gcd(b, cand)

gcd_res = 0
if a < b:
  gcd_res = gcd(b, a)
else:
  gcd_res = gcd(a, b)

count = 1
for i in reversed(range(1, 101)):
  if (gcd_res % i) == 0:
    if count == k:
      print(i)
      break
    count += 1
