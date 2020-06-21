"""to run the code you need to send 2 arguments
the first argument is the encryption either AES or DES
the second argument is the mode either CTR or ECB

Students:
Leen Kilani 0154493
Mostafa Al-Mohtaseb 0154526
"""


def encrypt(key, message, encryption, mode):
    key = bytes.fromhex(key)
    ciphertext = []
    blocks = []
    cipher = ""

    if encryption == 'DES':
        # each blocks has 8 bytes
        blocks = [message[i:i + 8] for i in range(0, len(message), 8)]
        from Crypto.Cipher import DES
        if mode == 'CTR':
            from Crypto.Util import Counter
            counter = Counter.new(64)
            cipher = DES.new(key, DES.MODE_CTR, counter=counter)
        elif mode == 'ECB':
            cipher = DES.new(key, DES.MODE_ECB)

    elif encryption == 'AES':
        # each block is 16 bytes
        blocks = [message[i:i + 16] for i in range(0, len(message), 16)]
        from Crypto.Cipher import AES
        if mode == 'CTR':
            from Crypto.Util import Counter
            counter = Counter.new(128)
            cipher = AES.new(key, AES.MODE_CTR, counter=counter)
        elif mode == 'ECB':
            cipher = AES.new(key, AES.MODE_ECB)

    for i, block in enumerate(blocks):
        ciphertext.append(cipher.encrypt(block))
    ciphertext = ''.join(list(map((lambda x: x.hex()), ciphertext)))
    ciphertext = bytes.fromhex(ciphertext)
    return ciphertext


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
        # print(key)
    with open('msg.txt', 'r') as message:
        message = bytes(message.read(), encoding='utf-8')

    if len(message) % (len(key) / 2) != 0:
        print("error: message length is not a multiple of key length\n")
        print("message size: {} bytes\n".format(len(message)))
        print("key size: {} bytes\n".format(len(key) / 2))
        exit()

    ciphertext = encrypt(key, message, encryption, mode)
    print(ciphertext.hex())
    with open('ctext.txt', 'w') as c:
        c.write(ciphertext.hex())
