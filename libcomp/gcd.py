def gcd(x, y):
    if x < y:
        x = x ^ y
        y = x ^ y
        x = x ^ y
    div = x % y
    while div != 0:
        x = y
        y = div
        div = x % y
    return y

def lcm(x, y):
    return x*y//gcd(x, y)
