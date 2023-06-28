def find_max_num (a, b, c):
# if condition is true then its the max number
    if a >= b and a >= c:
        max_num = a

    elif b >= a and b >= c:
        max_num = b
    else:
        max_num = c
    print(f"The max number of is {max_num}")

# Data
num = find_max_num (124, 21, 320)

