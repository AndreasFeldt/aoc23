def extract_first_last_unique_digits(input_string):
    digits = set()

    for char in input_string:
        if char.isdigit():
            digits.add(char)

    first_digit = None
    last_digit = None

    for digit in input_string:
        if digit in digits:
            first_digit = digit
            break

    for digit in reversed(input_string):
        if digit in digits:
            last_digit = digit
            break

    return first_digit, last_digit

numbers = open('input.txt').readlines()
num = 0
for string in numbers:
    first, last = extract_first_last_unique_digits(string)
    if first is not None and last is not None:
        new_num = int(f"{first}{last}")
        num += new_num
print(num)