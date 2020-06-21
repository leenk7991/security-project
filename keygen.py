"""to run the code you need to send an argument
the argument should be either AES or DES
this code generates a key of a certain size depending on the encryption mode

Students:
Leen Kilani 0154493
Mostafa Al-Mohtaseb 0154526
"""


def keygen(mode):
    import secrets
    randomKey = secrets.token_hex(8)  # default DES
    if mode == 'DES':
        randomKey = secrets.token_hex(8)
    elif mode == 'AES':
        randomKey = secrets.token_hex(16)

    return randomKey


if __name__ == '__main__':
    import sys

    mode = sys.argv[1]
    key = keygen(mode)
    print(key)
    with open('key.txt', 'w') as writefile:
        writefile.write(key)
