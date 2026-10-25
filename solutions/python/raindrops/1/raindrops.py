def convert(number):
    return_string = ""
    if not is_divisible(number):
        return str(number)
    if number % 3 == 0:
        return_string += "Pling"
    if number % 5 == 0:
        return_string += "Plang"
    if number % 7 == 0:
        return_string += "Plong"
    return return_string

def is_divisible(number):
    return number % 3 == 0 or number % 5 == 0 or number % 7 == 0