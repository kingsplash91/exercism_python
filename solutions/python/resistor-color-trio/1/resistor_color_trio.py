MAPPINGS = {
    'black':0,
    'brown':1,
    'red':2,
    'orange':3,
    'yellow':4,
    'green':5,
    'blue':6,
    'violet':7,
    'grey':8,
    'white':9
}

METRICS = {
    10**3:'kilo',
    10**6:'mega',
    10**9:'giga'
}
def value(colors):
    first_dig = MAPPINGS[colors[0]]
    second_dig = MAPPINGS[colors[1]]
    return int(str(first_dig)+str(second_dig))

def label(colors):
    val = value(colors)
    if val == 0:
        return '0 ohms'
    # 10^color_value allows for there to be n amount of trailing 0s
    zeroes = 10 ** MAPPINGS[colors[2]]
    result = val * zeroes

    if zeroes not in METRICS.keys():
        if result % 1000 == 0:
            return str(int(result/1000)) + " kiloohms"
        return str(result) + " ohms"
         
    return str(int(result/zeroes)) + " " + METRICS[zeroes] + "ohms"
