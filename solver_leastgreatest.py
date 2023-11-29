from pwn import *

s = remote("challs.xmas.htsp.ro", 6050)
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())

for i in range(100):
    print (s.readline())
    x = int(s.readline().split(b"= ")[1][:-1])
    y = int(s.readline().split(b"= ")[1][:-1])
    r = y // x
    ans = 1
    for i in range(2, 10**6):
        if r % i == 0:
            ans *= 2
            while r % i == 0:
                r = r // i
    s.sendline(str(ans))
    print (s.readline())
while 1:
    print (s.readline())
