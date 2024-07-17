import math
def generate_keys(p, q):
  # ここに E, D, N を求める処理を実装する。
  n = p*q
  L =math.lcm(p-1,q-1)
  for i in range(2,L):
    if gcd(i,L) ==1:
    E=i
    break
  for i range(2,L):
    if(E*i) % L == 1:
    D=i
    break
  # (E, N) が公開鍵で (D, N) が秘密鍵を表す。
  return (E, N), (D, N)

def encrypt(plain_text, public_key):
  '''
  公開鍵 public_key を使って平文 plain_text を暗号化する。
  '''
  E, N = public_key
  plain_integers = [ord(char) for char in plain_text]
  encrypted_integers = [pow(i, E, N) for i in plain_integers]
  encrypted_text = ''.join(chr(i) for i in encrypted_integers)

  return encrypted_text

def decrypt(encrypted_text, private_key):
  '''
  秘密鍵 private_key を使って暗号文 encrypted_text を復号する。
  '''
  D, N = private_key
  encrypted_integers = [ord(char) for char in encrypted_text]
  decrypted_intergers = [pow(i, D, N) for i in encrypted_integers]
  decrypted_text = ''.join(chr(i) for i in decrypted_intergers)

  return decrypted_text
  
value = input(/n'encrypt::1'/n'decrypt::2')
p =
q =
e =
if value==1:

if valie==2:

print(n)

G =math.gcd(p-1,q-1)
print(L,G)
#de-yL=1
#d*3-20*y=1 ←一次不定式
#ユークリッドを使う
#20=3*6+2
#3 =2*1+1　→　1=3-(2*1)　→　1=3-(20-(3*6))*1 → 1=3-(20*1)-(3*6) →　1=-(20*1)+(3*7)
#d=7,y=1
#inverse(E,(q-1)*(p-1))の処理内容
#n*d mod M = 1
#55*d mod M = 1
#d=

