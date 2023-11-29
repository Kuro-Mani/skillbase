import time
from pwn import *
from random import SystemRandom
from fractions import gcd

def greedy(v, sub, diff, maxSteps, totalSteps):
    for val in v:
        val -= sub
        if val <= 0:
            continue
        val = val // diff + (val % diff != 0)
        if val > maxSteps:
            return False
        totalSteps -= val
        if totalSteps < 0:
            return False
    return True

def binarySearch(v, n, k, x, y):
    maxval = max(v)
    left, right, last = 0, maxval, maxval
    while left <= right:
        mid = (left + right) // 2
        if greedy(v, mid * x, y - x, mid, mid * (n - k)):
            last = mid
            right = mid - 1
        else:
            left = mid + 1
    return last

def solve(n, k, x, y, v):
    if x > y:
        x, y, k = y, x, n - k
    if x == y:
        return max([a // x + (a % x != 0) for a in v])
    return binarySearch(v, n, k, x, y)

class lcg:
    def __init__(self, rndgen, modulo, x0 = None, a = None, c = None):
        if x0 == None:
            x0 = rndgen.randint(2, modulo - 1)
        
        if a == None:
            a = rndgen.randint(2, modulo - 1)
            while gcd(a, modulo) != 1:
                a = rndgen.randint(2, modulo - 1)
        
        if c == None:
            c = rndgen.randint(2, modulo - 1)
            while gcd(c, modulo) != 1:
                c = rndgen.randint(2, modulo - 1)
        
        self.a = a
        self.c = c
        self.mod = modulo
        self.x0 = x0
        self.x = x0

    def next(self):
        o = self.x
        self.x = (self.a * self.x + self.c) % self.mod
        return o

s = remote("challs.xmas.htsp.ro", 6055)
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())

for i in range(100):
    starttime = time.time()
    print (s.readline())
    
    x = s.readline().replace(b"\n",b"").split(b",")
    n = int(x[0].split(b"= ")[1])
    k = int(x[1].split(b"= ")[1])
    
    x = s.readline().replace(b"\n",b"").split(b",")
    p = int(x[0].split(b"= ")[1])
    q = int(x[1].split(b"= ")[1])
    
    v = []
    x = s.readline().replace(b"\n",b"").split(b",")
    v1 = int(x[0].split(b"= ")[1])
    a = int(x[1].split(b"= ")[1])
    c = int(x[2].split(b"= ")[1])
    mod = int(x[3].split(b"= ")[1])
    gen = lcg(SystemRandom(), mod, v1, a, c)

    print ("recving:",time.time() - starttime)
    starttime = time.time()
    for i in range(n):
        v.append(gen.next())
    ans = solve(n, k, p, q, v)
    s.sendline(str(ans))
    s.recvline()
    
    print ("calculation:", time.time() - starttime)
    print (s.recvline())
while 1:
    print (s.readline())
