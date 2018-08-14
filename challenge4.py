from challenge3 import single_byte_xor
import string

filename = 'challenge4data.txt'

with open(filename, 'r') as f:
    all_line_results = []
    for line_num, line in enumerate(f):
        line_key_results = []
        for i in range(256):
            line_key_results.append([single_byte_xor(line.rstrip(), i), line_num, i, line])

        best_guess = max(line_key_results, key=lambda s: s[0].count(' '))

        un_print = [x for x in best_guess[0] if x not in string.printable]

        if not un_print:
            all_line_results.append(best_guess)

    # print(all_line_results)

    for x in all_line_results:
        print("Deciphered line " + str(x[1]) + " with key " + str(hex(x[2])) + " (ascii character " + chr(x[2]) + ")")
        print("Original line: \"" + str(x[3]).rstrip() + "\"")
        print("Deciphered message: \"" + str(x[0]).rstrip() + "\" ")
