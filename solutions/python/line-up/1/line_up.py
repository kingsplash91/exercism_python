def line_up(name, number):
    suffix = ""

    if str(number).endswith('1') and not str(number).endswith('11'):
        suffix = "st"
    elif str(number).endswith('2') and not str(number).endswith('12'):
        suffix = "nd"
    elif str(number).endswith('3') and not str(number).endswith('13'):
        suffix = "rd"
    else:
        suffix = "th"

    return f'{name}, you are the {str(number)}{suffix} customer we serve today. Thank you!'