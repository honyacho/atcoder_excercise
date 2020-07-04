inmap=input()

odd = {'0':0, '1':0}
ev = {'0':0, '1':0}
for i, tile in enumerate(inmap):
    if i % 2:
        odd[tile] += 1
    else:
        ev[tile] += 1

print(min( ev['0'] + odd['1'] , ev['1'] + odd['0'] ))
