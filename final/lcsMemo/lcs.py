import sys
import time

def lcs(str_1, str_2):
    len_1, len_2 = len(str_1), len(str_2)

    memo = make_array(1+len_1, 1+len_2)

    ss = lcs_inner(
        str_1, str_2,
        len_1, len_2,
        memo,
    )

    # for row in memo:
    #     elems = ['{:>5.5s}'.format(elem) for elem in row]
    #     print('{}'.format(' , '.join(elems)))

    return ss

def lcs_inner(str_1, str_2, len_1, len_2, memo):
    if memo[len_1][len_2] is None:
        # print('{},{}'.format(len_1, len_2))

        if (len_1 == 0) or (len_2 == 0):
            memo[len_1][len_2] = ''
        elif str_1[len_1-1] == str_2[len_2-1]:
            lcs = lcs_inner(str_1, str_2, len_1-1, len_2-1, memo) + str_1[len_1-1]
            memo[len_1][len_2] = lcs
        else:
            lcs_1 = lcs_inner(str_1, str_2, len_1-1, len_2,   memo)
            lcs_2 = lcs_inner(str_1, str_2, len_1,   len_2-1, memo)
            if len(lcs_1) > len(lcs_2):
                memo[len_1][len_2] = lcs_1
            else:
                memo[len_1][len_2] = lcs_2

    return memo[len_1][len_2]

def make_array(nrows,ncols):
    arr = []
    for _ in range(nrows):
        arr.append([None]*ncols)
    return arr


if __name__ == '__main__':
    if True:
        str_1, str_2 = sys.argv[1], sys.argv[2]
        # str_1, str_2 = 'XMJYAUZ', 'MZJAWXU'
        # str_1, str_2 = 'abcdefg', 'xaxcxexgx'

        start = time.time()

        print('{}'.format(lcs(str_1, str_2)))

        elapsed = time.time() - start
        print('elapsed = {:1.3e}'.format(elapsed))
    else:
        sys.setrecursionlimit(10000)
        str_1 = 'ACCGTCTTAGCGATCAACACATTTAACAACGCGCCGCACCCCCCGTCAAACGAGCTTTTGGGCTCTTGTCCTTTTACAAGCTTCACGACGCATACAGCCTTGATCAACGGTTTGATCTGTCTCCCTTCAGCTGGCTTTAAAGGACATACATATGAAGGCCTTAATAAGGTCCGGGAACTCCACATATTCGGTACTGGGCAAACCCCATGAACCACCTCAACATGAAGAGTCCGAGGACTCTCACGATCCACCAATGCAGATCGGAACTGTGCGATCGCGTAATGAGCCGAGTACTTGGTTTGTGTTTAGGTTATGGGGGCCGGGAGCCGGTTCAATATAAGGAAGTAGTTGCAGATTAGTTGTTGCGAACGGTCATAAATTTGATGGGTAAACGTGAACTTAACAAACCGTGATAGCTAATCCTATGCATCCCTTACGTGGATCGACTCGAGTACCCAGGTGAACCGACTACTTGATAACCGGAAATCGCGGTATAAAAGCGCTCACGGTCAGGAGATATACCTCCAAGCAGTAGTCTTTCTGAGCCTAGAGTAGTAAATTACAGGGACGATGTCTTTTACCGAGGCAACATTTTATTGAGAATCACATGAGGCACAGGTAAAGGCGACATCACGATCGAGATCAACCCCTACTTGTTCAAAACATTGAGAACCAGCTCTGTTTTGGAACCTAGAAAGATAACGCATCCGCTTGATATTCCACGGCTTGTCCCTCTTGTGCGGTCCATCTATCGGAGTTTCCTCCGATACGACCCGCAATGTTTCCAGGCGTACGGTACTTTATGAATACACTCGCGCTGTAACCTGTTATGTGAAACACACACGACAGAGCTTCGCGTGGGCCCAGCGACCCGGTAATACTACATCACCGCACACGACCTCGAGCAGTCTTTGCCGGCGTCCGTAAGTAGTCTAAAGTTGTGTTGATGCTTGGGGTTAAAGCTAAATCGTCCGCAGAATACGACTCTCATCCCAAT'
        str_2 = 'ACCCGCACGCGCTTTGGTCTAGATTCTAGCTCCAACTTGCCTGCTAGATACTCTGTTAAAAGATGGTTTTACAACCCCCTCCTCTGTCCCTGGGGTATTATATAATACGTCGGATAGTCAGGTACAAATACAAGTGGGTGGGAATACTTTTCCTCGGATCCTAGACCACGGATTACTGCGTGGTTGACAAGAGTCGGCCCGGAGGGAAACGTGAAGGTTAGTGCAATTAAAGTCTCTAATGTGAAGCCTCCGCGAAGCGAGGAGTTTCTGAGATCGAGTACTATTTAGAGTTCGAAATCACGGCTTAACCTCACTGCCACGCATAACTTGCCGGCAATCCAGTTTTGCAACGATACTTAATTTGTGCAGCTCATCTTTGCTGTCCAGAAATAGAGCTAGTCGATCTCATCTTGCGGGTAGCCAGAAGTCCTACCGTCTCCTCCATGTAGCTTAAAAATTTCGGTGAGGATCAAAAATGATAAACGTGACAGGTAAGCTCCTACGTCTATCCTATGACCCCCGCGGCAGAATAGGTTGGTAGTGTTAGTGCGTGAGCTGGTAGAATAGAGCACACTTAGGGAAACGGGAACCGTTATGTAGGGCTGCGACACACAAAAAAGTGTTCGTTGGTAAGCTGCCTCTCCACTAAACAGGATTTCTCTGGATGATCCCATCGAAGCAAGTTACGCACCACGCCGAGGCGGACCCTGGTACTAGCTGCCCCCCCCTTTATGGGGCGCTCGTACATCAAGATGATCGCGGACTCAACCTGATTACGAGTTGTCCAAGTAGTCCAGGGTAAGAGAAACTGGAGAGA'
        tlcs  = 'ACCGCAGCGTCAATTTACAACGCCGCACCGTAAAGATGGTTTTACAACCCCCTCCCTGTCCGGTTTATTTCTCTAGTCAGGACAAATAAAGTGGTGGGAATACTTTCTCGGACCAGACCACTACTGGTGGTTGACAAGAGTCGGCCCGGAGGGAACTGGTTGTGTTAGTTATGGGCCCCGGAAGGAGAGTTGAGATCGAGTCTATTTGAGTCGAATCACGGCTAACCTATGCACCTACTTGCCGATCCAGTGAACGATACTTATACCATCGCGTAAAAAGGCTAGTCGATATCCTCCAGAGTAGTCTTCTGAGCTAAAAATTCGGGAGATCAAAAATATAAACTGACAGGTAAGCCTACGTCATCAACCCCCGCAAAATTGGAGTGTTTTGGCTAGAAAGAGCACCTTGAAACGGGCCTTTGTGGGTCCACACAGTTTCTGTAAGCTGTTCCACTACGGTCTTATGATCATCGGCAAGTTAGCACCACGCGAGGCGGACCCGGTACTACTCCCCCACGCTCGACATCTTGCGGCTCCTGATTAAGTTGTGTGTCGGGTAAAGAAACTGAGAGA'

        alcs = lcs(str_1, str_2)

        # print('T = {}'.format(tlcs))
        print('A = {}'.format(alcs))

        # if alcs == tlcs:
        #     print('oh yeah!')
        # else:
        #     print('doh!')
