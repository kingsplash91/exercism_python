def is_armstrong_number(number):
    digits = [int(digit) for digit in str(number)]
    power = len(digits)

    total = 0

    for digit in digits:
        total += digit ** power

    if total == number:
        return True
    return False
