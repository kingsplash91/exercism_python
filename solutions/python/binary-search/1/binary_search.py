def find(search_list, value):
    if len(search_list) == 0:
        raise ValueError("value not in array")

    val = bst(search_list, value)
    if val == None:
        raise ValueError("value not in array")

    for idx, num in enumerate(search_list):
        if val == num:
            return idx

def bst(lis, value):
    if len(lis) == 1:
        if value == lis[0]:
            return value
        else:
            return None

    middle = len(lis) // 2

    if value == lis[middle]:
        return value

    if value > lis[middle]:
        return bst(lis[middle:], value)

    if value < lis[middle]:
        return bst(lis[:middle], value)

    return None
