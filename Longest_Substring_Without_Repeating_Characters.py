# coding = utf8
def lengthOfLongestSubstring(s):
    max_length_str = ''
    sub_str = ''
    for index, x in enumerate(s):
        if x in sub_str:
            if(len(max_length_str) < len(sub_str)):
                max_length_str = sub_str
            sub_str = sub_str[sub_str.index(x) + 1:]
            sub_str += x
        else:
            sub_str += x

        if index == len(s) - 1 and len(max_length_str) < len(sub_str):
            max_length_str = sub_str
    return len(max_length_str)

if __name__ == '__main__':
    s = 'fasd'
    print lengthOfLongestSubstring(s)
