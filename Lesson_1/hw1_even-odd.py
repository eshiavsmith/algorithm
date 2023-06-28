# Count odd and even numbers. Count odd and even digits of the whole number.
# Example: number is 34560, then 3 digits will be even (4, 6, and 0) and 2 odd digits (3 and 5).


def countEvenOdd(n):
# Initialize event_count and odd count
    even_count = 0
    odd_count = 0

    while n > 0:
        rem = n % 10
# if condition is true then increment even count
        if rem % 2:
            odd_count += 1
# increment even count
        else:
            even_count += 1
        n = int(n / 10)

    print(f"Odd count: {odd_count}, Even count: {even_count}")


test_num = 34560
countEvenOdd(test_num)