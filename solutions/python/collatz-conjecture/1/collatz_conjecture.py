def steps(number):
    if number < 1:
        raise ValueError("Only positive integers are allowed")
    current_number = number
    step = 0
    while current_number != 1:
        if current_number % 2 == 0:
            current_number = current_number / 2
        else:
            current_number = (current_number * 3) + 1
        step += 1
    return step