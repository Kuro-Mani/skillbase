from pwn import *
nc = remote('challs.xmas.htsp.ro', 6051)
for i in range(7):
    chall = nc.recvline().decode().strip()
i = 0
while True:
    test = nc.recvline().decode().strip()
    print(test)
    exec(nc.recvline().decode().strip())
    exec(nc.recvline().decode().strip())
    exec(nc.recvline().decode().strip())
    array = sorted(array)
    answer = str(array[:k1]) + '; ' + str(array[-k2:][::-1])
    answer = answer.replace('[', '')
    answer = answer.replace(']', '')
    nc.sendline(answer)
    i += 1
    if i == 50:
        check = nc.recv().decode().strip()
        print(check)
        break
    else:
        check = nc.recvline().decode().strip()
        print(check)