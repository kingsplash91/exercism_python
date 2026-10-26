def rotate(text, key):
    rotated_text = ""
    for c in text:
        if c.isupper():
            c = chr(((ord(c) - ord('A')) + key) % 26 + ord('A'))
        elif c.islower():
            c = chr(((ord(c) - ord('a')) + key) % 26 + ord('a'))
        rotated_text+=c

    return rotated_text
        
