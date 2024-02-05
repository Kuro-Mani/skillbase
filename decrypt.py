from Crypto.Util.number import long_to_bytes
import sys
sys.set_int_max_str_digits(7000)
# nをファイルから読み込む
with open("./n.txt", "r") as file:
    n = int(file.read())

# dをファイルから読み込む
with open("./d.txt", "r") as file:
    d = int(file.read())

# 暗号文e_textをファイルからバイナリ形式で読み込む
with open("./e_text.txt", "rb") as file:
    e_text = int.from_bytes(file.read(), byteorder="big")

# 暗号文を復号
decrypted_message = pow(e_text, d, n)

# 復号されたメッセージをバイト列に変換
decrypted_text = long_to_bytes(decrypted_message).decode("utf-8")

print("Decrypted Message:", decrypted_text)
