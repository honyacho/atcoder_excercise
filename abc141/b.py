S=input()
kisuu={'R','U','D'}
guusuu={'L','U','D'}

res = True
for c in S[::2]:
    res = res and c in kisuu
for c in S[1::2]:
    res = res and c in guusuu

print('Yes' if res else 'No')
