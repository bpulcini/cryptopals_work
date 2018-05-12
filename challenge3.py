import binascii

hex_encoded_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
unhexedstr = binascii.unhexlify(hex_encoded_str)

all_results = []
for i in range(256):
    holder = []
    for x in unhexedstr:
        holder.append(chr(i ^ ord(x)))
    all_results.append(''.join([str(e) for e in holder]))


print max(all_results, key=lambda s: s.count(' '))
