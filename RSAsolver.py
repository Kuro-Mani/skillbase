from Crypto.util.number import *

c = int(input('c:'))
e = int(input('e:'))
p = int(input('p:'))
q = int(input('q:'))
n = p*q

phi_n = (p-1)*(q-1)
d = pow(e,-1,phi_n)
m = pow(c,d,n)
print(long_to_bytes(m))