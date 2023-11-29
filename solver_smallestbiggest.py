from pwn import *
from heapq import *

s = remote("challs.xmas.htsp.ro", 6051)
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())
print (s.readline())

for i in range(50):
    print (s.readline())
    arr = [int(a) for a in s.readline().split(b"= ")[1][1:-2].split(b",")]
    #print (arr)
    k1 = int(s.readline().split(b"= ")[1][:-1])
    k2 = int(s.readline().split(b"= ")[1][:-1])
    #print (k1, k2)
    h1 = []
    h2 = []
    arr1 = []
    arr2 = []
    heapify(h1)
    heapify(h2)
    for a in arr:
        heappush(h1, -a)
        heappush(h2, a)
        if len(h1) > k1:
            heappop(h1)
        if len(h2) > k2:
            heappop(h2)
    while len(h1) > 0:
        arr1.append(-heappop(h1))
    while len(h2) > 0:
        arr2.append(heappop(h2))

    arr1 = list(reversed(arr1))
    arr2 = list(reversed(arr2))
    #print (arr1, arr2)
    s.sendline('; '.join([', '.join(str(a) for a in arr1), ', '.join(str(a) for a in arr2)]))
    print (s.readline())
for i in range(2):
    print (s.readline())
