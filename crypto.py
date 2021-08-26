
from Crypto.Cipher import Salsa20

def encrypt(text, secret):

    cipher = Salsa20.new(key=secret)
    cipherObj = cipher.nonce + cipher.encrypt(text)
    return cipherObj


def decrypt(secret, cipherObj):

    msg_nonce = cipherObj[:8]
    ciphertext = cipherObj[8:]
    cipher = Salsa20.new(key=secret, nonce=msg_nonce)

    plaintext = cipher.decrypt(ciphertext)
    return plaintext