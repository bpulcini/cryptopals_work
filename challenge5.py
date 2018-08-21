from challenge2 import xor_two_hexes
import binascii

phrase = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"

key = "ICE"

expected = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

xor_key = (key * len(phrase))[:len(phrase)]

phrase_bin = bytes(phrase, 'utf-8')
phrase_hex = binascii.b2a_hex(phrase_bin)

xor_encoded_message = xor_two_hexes(phrase_hex, binascii.b2a_hex(xor_key.encode('utf-8'))).zfill(len(phrase_hex))

print(xor_encoded_message == expected)
