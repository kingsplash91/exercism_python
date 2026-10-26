def is_valid(isbn):
    no_hyphens = isbn.replace("-", "")

    # If ISBN is less than 10 equation can not be used, resulting in invalid.
    if len(no_hyphens) != 10:
        return False
    return equation(no_hyphens) % 11 == 0
    
def equation(d):
    uppercase_list = [chr(i) for i in range(65, 91)]
    uppercase_list.remove('X')
    d_list = []

    # The isbn can end with X to be represented as 10
    if 'X' in d and not d.endswith('X'):
        return -1

    # Make sure no characters exist within the equation
    if not set(uppercase_list).isdisjoint(set(d)):
        return -1
        
    for i in d:
        if i == 'X':
            d_list.append(10)
        else:
            d_list.append(int(i))
            
    return (d_list[0] * 10 + d_list[1] * 9 + d_list[2] * 8 + 
            d_list[3] * 7 + d_list[4] * 6 + d_list[5] * 5 + 
            d_list[6] * 4 + d_list[7] * 3 + d_list[8] * 2 + d_list[9] * 1)