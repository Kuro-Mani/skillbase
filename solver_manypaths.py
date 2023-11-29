from pwn import *

def matmul(a, b, mod):
    n = len(a)
    m = len(a[0])
    p = len(b[0])
    c = [[0 for i in range(m)] for j in range(p)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                c[i][j] = (c[i][j] + a[i][k] * b[k][j]) % mod
    return c

def matpow(m, d, mod):
    if d == 1:
        return m
    r = matpow(m, d // 2, mod)
    r = matmul(r, r, mod)
    if(d & 1 == 1):
        return matmul(r, m, mod)
    return r

def solve(n, m, bl, d, mod):
    for b in bl:
        for i in range(1, n + 1):
            m[i - 1][b - 1] = 0
            m[b - 1][i - 1] = 0
    m = matpow(m, d, mod)
    return m[0][n - 1]

s = remote("challs.xmas.htsp.ro", 6053)
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())

for i in range(40):
    print (s.readline())
    N = int(s.readline().split(b"= ")[1][:-1])
    print ("N:", N)
    mat = []
    s.readline()
    for i in range(N):
        mat.append([int(a) for a in s.readline().split(b",")])
    print ("mat:", mat)
    blockers = []
    for a in s.readline().split(b"[")[1].split(b"]")[0].split(b","):
        try:
            blockers.append(int(a))
        except:
            pass
    print ("bl:", blockers)
    d = int(s.readline().split(b"= ")[1][:-1])
    print ("d:", d)
    s.readline()
    ans = solve(N, mat, blockers, d, 666013)
    print("ans:", ans)
    s.sendline(str(ans))
    print (s.readline())

print (s.recv())
