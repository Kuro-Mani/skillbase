from sympy import mod_inverse
import sys
sys.set_int_max_str_digits(20000)

def calculate_private_key(p, q, e):
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)
    return d

# 例として、素数 p, q, 公開鍵 e を指定
p = 2**9941-1
q = 2**11213-1 
e = 65537

# 秘密鍵 d の計算
d = calculate_private_key(p, q, e)

print("Private Key (d):", d)
