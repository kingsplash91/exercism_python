def append(list1, list2):
    return list1 + list2


def concat(lists):
    new_list = []

    for l in lists:
        new_list = new_list + l

    return new_list


def filter(function, list):
    new_list = []

    for i in list:
        if function(i):
            new_list.append(i)
            
    return new_list

def length(list):
    count = 0

    for i in list:
        count+=1

    return count

def map(function, list):
    new_list = []

    for i in list:
        new_list.append(function(i))

    return new_list


def foldl(function, list, initial):
    result = initial 
    for i in list:
        result = function(result, i)

    return result


def foldr(function, list, initial):
    result = initial 
    for i in list[::-1]:
        result = function(result, i)

    return result


def reverse(list):
    return list[::-1]
