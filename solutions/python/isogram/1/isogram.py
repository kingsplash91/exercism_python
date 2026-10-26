def is_isogram(phrase):
    if len(phrase) == 0 or len(phrase) == 1:
        return True
        
    no_space = phrase.replace(" ", "")
    no_hyphens = no_space.replace("-", "")
    no_hyphens = no_hyphens.upper()

    phrase_dict = {}

    for character in no_hyphens:
        if character not in phrase_dict.keys():
            phrase_dict[character] = 1
        else:
            phrase_dict[character] += 1

    set_values = set(phrase_dict.values())

    if set_values != {1}:
        return False

    return True
