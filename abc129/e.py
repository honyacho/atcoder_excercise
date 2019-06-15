MOD,L,pat1,pat2 = 1000000007,input(),1,0
for i in range(0,len(L)): pat1,pat2 = (pat1*2%MOD,(pat1+pat2*3)%MOD) if L[i] == '1' else (pat1,pat2*3%MOD)
print((pat1+pat2)%MOD)
