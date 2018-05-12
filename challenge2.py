str_1_hex = "1c0111001f010100061a024b53535009181c"
str_2_hex = "686974207468652062756c6c277320657965"
expected_output_hex = "746865206b696420646f6e277420706c6179"


def xor_two_hexes(input_1, input_2):

    bin1 = bin(int(input_1, 16))
    bin2 = bin(int(input_2, 16))

    xor_bin = bin(int(bin1, 2) ^ int(bin2, 2))
    xor_int = int(xor_bin, 2)
    xor_hex_string = format(xor_int, 'x')
    return xor_hex_string


print xor_two_hexes(str_1_hex, str_2_hex) == expected_output_hex

