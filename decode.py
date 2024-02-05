from Crypto.Util.number import *
with open('flag.enc', 'rb') as f:
    c = bytes_to_long(f.read())　# file read 
# c = int(input('c: '))　# int read
e = int(input('e: '))
p = int(input('p: '))
q = int(input('q: '))
n = p * q
phi_n = (p-1) * (q-1)
d = pow(e, -1,phi_n)
m = pow(c,d,n)
print(long_to_bytes(m))
