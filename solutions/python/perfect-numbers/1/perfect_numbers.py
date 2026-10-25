def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if summation(divisors(number)) == number:
        return "perfect"
    if summation(divisors(number)) > number:
        return "abundant"
    return "deficient"

def summation(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum

def divisors(number):
    if number == 1:
        return []
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")
    lower_div = []
    upper_div = []
    
    for i in range(1, int(number ** .5) + 1):
        if number % i == 0:
            lower_div.append(i)
            if i != number // i and i != 1:
                upper_div.append(number // i)
    print(lower_div, upper_div)
    return lower_div + upper_div[::-1]
