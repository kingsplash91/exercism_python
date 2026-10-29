def find_anagrams(word, candidates):
    word_list = list(word.lower())
    
    anagrams = []

    for c in candidates:
        if word.lower() != c.lower():
            if sorted(word_list) == sorted(list(c.lower())):
                anagrams.append(c)
    return anagrams