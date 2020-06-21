"""to run the code you need to send 2 arguments
the first argument is the encryption either AES or DES
the second argument is the mode either CTR or ECB

Students:
Leen Kilani 0154493
Mostafa Al-Mohtaseb 0154526
"""


def decrypt(key, c, encryption, mode):
    key = bytes.fromhex(key)
    c = bytes.fromhex(c)
    plaintext = []
    blocks = []
    cipher = ""
    if encryption == 'DES':
        # each blocks has 8 bytes
        blocks = [c[i:i + 8] for i in range(0, len(c), 8)]
        from Crypto.Cipher import DES
        if mode == 'CTR':
            from Crypto.Util import Counter
            counter = Counter.new(64)
            cipher = DES.new(key, DES.MODE_CTR, counter=counter)
        elif mode == 'ECB':
            cipher = DES.new(key, DES.MODE_ECB)

    elif encryption == 'AES':
        # each block is 16 bytes
        blocks = [c[i:i + 16] for i in range(0, len(c), 16)]
        from Crypto.Cipher import AES
        if mode == 'CTR':
            from Crypto.Util import Counter
            counter = Counter.new(128)
            cipher = AES.new(key, AES.MODE_CTR, counter=counter)
        elif mode == 'ECB':
            cipher = AES.new(key, AES.MODE_ECB)

    for i, block in enumerate(blocks):
        plaintext.append(cipher.decrypt(block))
    plaintext = ''.join(list(map((lambda x: x.hex()), plaintext)))
    plaintext = bytes.fromhex(plaintext)
    return plaintext


if __name__ == '__main__':
    import sys

    encryption = sys.argv[1]  # AES or DES
    mode = sys.argv[2]  # CTR or ECB

    if not (encryption == 'AES' or encryption == 'DES'):
        print("wrong encryption mode\n")
        exit()
    if not (mode == 'CTR' or mode == 'ECB'):
        print("wrong encryption mode\n")
        exit()

    with open("key.txt", 'r') as keyfile:
        key = hex(int(keyfile.read(), 16)).lstrip('0x').rstrip('L')

    with open('ctext.txt', 'r') as c:
        c = hex(int(c.read(), 16)).lstrip('0x').rstrip('L')

    if len(c) % len(key) != 0:
        c=''.join(["0",c])

    plaintext = decrypt(key, c, encryption, mode)
    print(plaintext.decode("utf-8"))
    with open("plaintext.txt", 'w') as p:
        p.write(plaintext.decode("utf-8"))
