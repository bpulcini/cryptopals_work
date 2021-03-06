import binascii

def hex_to_b64(hex_string):
    return binascii.b2a_base64(binascii.unhexlify(hex_string), newline=False).decode('ascii')


hexed_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

print(hex_to_b64(hexed_string) == expected)
