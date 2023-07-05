def unique_str_char(s):
    lenstr = len(s)
    lenset = len(set(s))
    return lenset == lenstr

test_right = "aaabbccd"
test_wrong = "abcde"
print(unique_str_char(test_right))
print(unique_str_char(test_wrong))