from sympy import * 
from pwn import *

def countPairs(G, L):
    if L % G != 0:
        return 0
    if L == G:
        return 1
    n = L // G
    return 1 << len(primefactors(n))

if __name__ == "__main__":
    nc = remote('challs.xmas.htsp.ro', 6050)
    for i in range(5):
        chall = nc.recvline().decode().strip()
    i = 0
    while True:
        test = nc.recvline().decode().strip()
        print(test)
        G = int(nc.recvline().decode().strip()[12:])
        L = int(nc.recvline().decode().strip()[12:])
        answer = countPairs(G, L)
        nc.sendline(str(answer))
        i += 1
        if i == 100:
            check = nc.recv().decode().strip()
            print(check)
            break
        else:
            check = nc.recvline().decode().strip()
            print(check)