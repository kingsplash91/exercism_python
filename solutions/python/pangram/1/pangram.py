def is_pangram(sentence):
    # Uppercase (ASCII 65 to 90)
    uppercase_list = [chr(i) for i in range(65, 91)]

    character = set(uppercase_list)
    sentence_as_set = set(sentence.upper())
    
    return character.issubset(sentence_as_set)
