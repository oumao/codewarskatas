def disemvowel(string_):
    vowels = ["a", "e", "i", "o", "u"]

    for char in string_:
        if char.lower() in vowels:
            string_ = string_.replace(char, "")
    return string_