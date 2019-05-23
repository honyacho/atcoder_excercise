S=input()
prev=int(S[:2])
aft=int(S[2:])

if prev <= 12 and prev >= 1:
    if aft == 0:
        print("MMYY")
    elif aft <= 12:
        print("AMBIGUOUS")
    else:
        print("MMYY")
elif prev > 12:
    if aft == 0:
        print("NA")
    elif aft <= 12:
        print("YYMM")
    else:
        print("NA")
else:
    if aft >= 1 and aft <= 12:
        print("YYMM")
    else:
        print("NA")
