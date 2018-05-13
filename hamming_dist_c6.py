string1 = "this is a test"
string2 = "wokka wokka!!!"

bin_1_a = ''.join([format(ord(c), 'b').zfill(8) for c in string1])
bin_2_a = ''.join([format(ord(c), 'b').zfill(8) for c in string2])


def get_hamming_dist(bin_1, bin_2):
    if len(bin_1) > len(bin_2):
        bin_2.zfill(len(bin_1))
        print "length of binary data not the same"
    elif len(bin_2) > len(bin_1):
        bin_1.zfill(len(bin_2))
        print "length of binary data not the same"

    hamming_dist = 0
    for i in range(len(bin_1)):
        if bin_1[i] != bin_2[i]:
            hamming_dist += 1

    return hamming_dist


if __name__ == "__main__":
    print get_hamming_dist(bin_1_a, bin_2_a)
