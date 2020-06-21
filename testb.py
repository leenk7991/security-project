"""to run the code you need to send 2 arguments
the first argument should be either AES or DES
the second argument should be either CTR or ECB
this code will test the given encryption mode for the most occurring byte

Students:
Leen Kilani 0154493
Mostafa Al-Mohtaseb 0154526
"""

import encrypt
import keygen
import sys

encryption = sys.argv[1]
mode = sys.argv[2]
with open("textb.txt", 'r') as A:
    text = bytes(A.read(), encoding='utf-8')
ctext = encrypt.encrypt(keygen.keygen(encryption), text, encryption, mode)
bytelist = [byte for byte in ctext]

from collections import Counter

bytedict = Counter(bytelist)
maximum = 0
maxkey = 0
for k, v in bytedict.items():
    if v > maximum:
        maximum = v
        maxkey = k
frequency = maximum / len(bytelist)

print("most occurring byte is :{} with frequency: {}\n".format(bytes([maxkey]), frequency))
