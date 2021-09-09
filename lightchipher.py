def code( letter, base ):
    return ord(letter) - ord(base)

def char( code ):
    return chr( code % 26 + ord('a') )

def encrypt( plain, key ):
    index = 0
    result = ''
    while index < len(plain):
        index2 = index % len(key)
        plain_code = code( plain[index], 'a' )
        key_code = code( key[index2], 'A' )
        result += char( plain_code + key_code )
        index += 1
    return result
 
def decrypt( cipher, key ):
    index = 0
    result = ''
    while index < len(cipher):
        index2 = index % len(key)
        cipher_code = code( cipher[index], 'a')
        key_code = code( key[index2], 'A' )
        result += char( cipher_code - key_code )
        index += 1
    return result


if __name__ == '__main__':
    plain_text = input("word input:")
    key = input("pass_key:")
    cipher_text = encrypt( plain_text, key )
    decode_text = decrypt( cipher_text, key )
    print( cipher_text )
    print( decode_text )