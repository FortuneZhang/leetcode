# coding=utf8
begin_position = 0


def main(s):
    all_10_letter_long_sequences_list = [
        s[x - 10:x] for x in range(10, len(s) + 1, 1)]
    sequences_dict = {}
    for x in all_10_letter_long_sequences_list:
        if x in sequences_dict:
            sequences_dict[x] += 1
        else:
            sequences_dict[x] = 0
    return [k for k, v in sequences_dict.iteritems() if v > 0]

if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    print main(s)
