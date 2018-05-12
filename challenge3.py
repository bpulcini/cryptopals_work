import binascii
from challenge2 import xor_two_hexes

hex_encoded_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

unhexedstr = binascii.unhexlify(hex_encoded_str)
print unhexedstr

# unhexed = int(hex_encoded_str, 16)
#print unhexed

# int_hexed_str = int(hex_encoded_str, 16)
# print int_hexed_str

min_letter_dec = ord('a')
max_letter_dec = ord('z')

# print min_letter_dec
# print max_letter_dec

#xor_two_hexes(hex_encoded_str, ord('e'))

# print unhexedstr
#
# print len(hex_encoded_str)
# print len(unhexedstr)
array_of_results = []

for i in range(0, 256):
    len_xor = len(unhexedstr)
    xor_cipher = format(i, 'x') * len_xor
    print xor_cipher.zfill(2)

    hex_xored = xor_two_hexes(hex_encoded_str, xor_cipher)
    #print hex_xored
    #array_of_results.append(binascii.unhexlify(hex_xored))

answer = max(array_of_results, key=lambda s: s.count(' '))