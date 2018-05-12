str_1_hex = "1c0111001f010100061a024b53535009181c"
str_2_hex = "686974207468652062756c6c277320657965"
expected_output_hex = "746865206b696420646f6e277420706c6179"


def xor_two_hexes(input_1, input_2):
    xor_bin = bin(int(input_1, 16) ^ int(input_2, 16))
    xor_hex_string = format(int(xor_bin, 2), 'x')
    return xor_hex_string


if __name__ == '__main__':
    print xor_two_hexes(str_1_hex, str_2_hex) == expected_output_hex

