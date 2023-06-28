# Compute the sum of digits in all numbers from 1 to n. When a function gets a number n, /
# find the sum of digits in all numbers from 1 to n.
# Example: n = 5. Result = 1 + 2 + 3 + 4 + 5 = 15

def sum_of_digits(number):
    digit_sum = 0
    for i in range(1, number+1):
        digit_sum = (digit_sum + i)

    print(f'sum of all digits result in {digit_sum} ')

digit = sum_of_digits(5)