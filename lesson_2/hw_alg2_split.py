def split_string(s):
    length=len(s)   #Determine length of string
    half = length // 2    #split string in half
    add = 0    #create and extra variable for strings with odd char
    if length % 2:
        add = 1  #add one char to be one char greater
    left = s[:half + add]
    right = s[half + add:]
    return right + left

test_str_odd = "bbbbbcaaaaa"
test_str_even = "bbbbbaaaaa"
print(split_string(test_str_odd))
print(split_string(test_str_even))