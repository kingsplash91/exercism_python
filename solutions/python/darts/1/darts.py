def score(x, y):

    # Calculate the distance of the point from (0, 0) with square root of (x2 - x1)^2 + (y2 - y1) ^2
    distance = ((x)**2 + (y)**2) ** 0.5

    
    if distance <= 1:
        return 10
    elif distance > 1 and distance <= 5:
        return 5
    elif distance > 5 and distance <= 10:
        return 1
    return 0
