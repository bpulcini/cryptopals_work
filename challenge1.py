import binascii

hexed_string = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
expected = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"


def hex_to_b64(input):
    return binascii.b2a_base64(binascii.unhexlify(input)).rstrip()


print hex_to_b64(hexed_string) == expected
