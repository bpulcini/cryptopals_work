import binascii

hex_encoded_str = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"


def single_byte_xor(hex_string, k):
    unhexed = binascii.unhexlify(hex_string)
    return ''.join([chr(k ^ x) for x in unhexed])


if __name__ == '__main__':
    all_key_tries = []
    for i in range(256):
        result = single_byte_xor(hex_encoded_str, i)
        all_key_tries.append([result, i])

    deciphered_text, key = max(all_key_tries, key=lambda s: s[0].count(' '))

    print("Deciphered string with key " + str(hex(key)) + " (ascii character " + chr(key) + ") and got messsage " + deciphered_text)
