def equilateral(sides):
    if verify_triangle(sides):
        return sides[0] == sides[1] == sides[2]
    else:
        return False


def isosceles(sides):
    if verify_triangle(sides):
        return sides[0] == sides[1] or sides[1] == sides[2] or sides[0] == sides[2]
    else:
        return False

def scalene(sides):
    if verify_triangle(sides):
        return sides[0] != sides[1] and sides[1] != sides[2] and sides[0] != sides[2]
    else:
        return False
        
def verify_triangle(sides):
    if 0 in sides:
        return False
    return (sides[0] + sides[1] > sides[2]) and (sides[1] + sides[2] > sides[0]) and (sides[0] + sides[2] > sides[1]) 