MOD = 1000000007
def LI(): return [int(x) for x in input().split()]
N,M = LI()

st = set()
for i in range(M):
    st.add(int(input()))

pat1 = 1
pat2 = 0

for i in range(1, N):
    tmp = pat2
    pat2 = pat1
    pat1 = ((pat1 + tmp)%MOD) if not i in st else 0

print((pat1+pat2)%MOD)
