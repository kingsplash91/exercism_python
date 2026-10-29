def commands(binary_str):
    actions_in_order = ['wink', 'double blink', 'close your eyes', 'jump']
    
    bstr_rev = binary_str[::-1]
    result = []
    for i in range(0, len(actions_in_order)):
        if bstr_rev[i] == '1':
            result.append(actions_in_order[i])
    
    # Check for reverse
    if bstr_rev[-1] == '1':
        result.reverse()

    return result