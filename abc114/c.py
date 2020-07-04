arr=[3,5,7]

global res
res = 0
ma = int(input())

def gen(num = 0):
    global res
    # print(num)
    if ma < num:
        return
    else:
        st = str(num)
        if st.count('3') and st.count('5') and st.count('7'):
            res += 1

    for i in arr:
        if num == 0:
            gen(num+i)
        else:
            gen(10*num + i)

gen()
print(res)
