"""
this code will test the keygen function for randomness
it will generate a 1000 and each time counting the occurrence of bit 0
it should be close to 0.5

Students:
Leen Kilani 0154493
Mostafa Al-Mohtaseb 0154526
"""

import keygen

count_list = []
for i in range(0,1000):
    count = 0
    k = keygen.keygen("DES")
    if len(k) != 16:
        print("wrong length {}",format(len(k)))
        exit()
    binary_k = bin(int(k, 16))[2:].zfill(64)
    for j in binary_k:
        if j == '0':
            count += 1
    count = count/64
    count_list.append(count)

avg = sum(count_list)/len(count_list)
print("average is {}\n".format(avg))



