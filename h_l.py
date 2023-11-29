#!/usr/bin/python3
import socket

def recvuntil(s, tail):
    data = b''
    while True:
        if tail in data:
            return data.decode()
        data += s.recv(1)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('challs.xmas.htsp.ro', 6051))

data = recvuntil(s, b'8\n').rstrip()
print(data)
data = recvuntil(s, b'\n').rstrip()
print(data)

for i in range(50):
    data = recvuntil(s, b'\n').rstrip()
    print(data)
    data = recvuntil(s, b'\n').rstrip()
    print(data)
    array = eval(data.split(' = ')[1])
    data = recvuntil(s, b'\n').rstrip()
    print(data)
    k1 = int(data.split(' = ')[1])
    data = recvuntil(s, b'\n').rstrip()
    print(data)
    k2 = int(data.split(' = ')[1])

    array.sort()
    ans = ', '.join(map(str, array[:k1]))
    ans += '; '
    ans += ', '.join(map(str, array[::-1][:k2]))
    print(ans)
    s.sendall(ans.encode() + b'\n')

    data = recvuntil(s, b'\n').rstrip()
    print(data)

data = recvuntil(s, b'\n').rstrip()
print(data)
data = recvuntil(s, b'\n').rstrip()
print(data)