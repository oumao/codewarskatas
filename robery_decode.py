def robbery_decode(sentence):
    const = list("bcdfghjklmnpqrstvwyxz")
    
    new_str = [] # array to contain strings after decoding

    # Retrieve all the characters in a sentence
    for char in list(sentence):

        # Retrieve all the constants in an Alphabet
        for letter in const:

            # compare if characters is lower
            if  char == letter.lower():
                new_str.append(char+"o"+char)
                break
            # compare if characters is upper
            elif char == letter.upper():
                new_str.append(char+"O"+char)
                break

        else:
            new_str.append(char)

    return ''.join(new_str)
print(robbery_decode("Hello World"))