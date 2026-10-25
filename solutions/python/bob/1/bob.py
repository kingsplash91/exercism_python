def response(hey_bob):
    hey_bob_stripped = hey_bob.strip()
    if len(hey_bob_stripped) != 0:
        if hey_bob_stripped.endswith("?") and not hey_bob_stripped.isupper():
            return "Sure."
        if not hey_bob_stripped.endswith("?") and hey_bob_stripped.isupper():
            return "Whoa, chill out!"
        if hey_bob_stripped.endswith("?") and hey_bob_stripped.isupper():
            return "Calm down, I know what I'm doing!"
            
    if hey_bob_stripped == "":
        return "Fine. Be that way!"
            
    return "Whatever."
