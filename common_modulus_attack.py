import gmpy

c1 = 
c2 = 

e1 = 
e2 = 
n = 
def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = egcd(b%a, a)
        return (g, x - (b // a) * y, y)

def modinv(a, m):
    g, x, y = egcd(a, m)
    return x % m

def commom_world(c1, c2, e1, e2, n):
    gcd, s1, s2 = egcd(e1, e2)
    print gcd
    print s1
    print s2
    if s1 < 0:
        s1 = -s1
        c1 = modinv(c1, n)
    elif s2 < 0:
        s2 = -s2
        c2 = modinv(c2, n)

    v = pow(c1, s1, n)
    w = pow(c2, s2, n)
    x = (v*w) % n
    return x

print commom_world(c1, c2, e1, e2, n)