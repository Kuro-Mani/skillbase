def long_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')

def egcd(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, x, y = egcd(b % a, a)
        return (g, y - (b // a) * x, x)

def main():
    c_st = input('c::')
    c = int(c_st)
    n_st = input('n::')
    n = int(n_st)
    e_st = input('e::')
    e = int(e_st)

    p_st = input('p::')
    p = int(p_st)
    q_st = input('q::')
    q = int(q_st)
    
    phi = (p - 1) * (q - 1)
    d = egcd(e, phi)[1]
    if d < 0:
        d += phi

    m = pow(c, d, n)
    flag = long_to_bytes(m)
    print(flag)

if __name__ == '__main__':
    main()