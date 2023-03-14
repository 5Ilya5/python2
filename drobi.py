def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x
 
def add(a, b, c, d):
    x = a*d + b*c
    y = b*d
    z = gcd(x, y)
    return (x//z, y//z)