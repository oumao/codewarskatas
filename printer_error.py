def printer_error(s):
    """
        Print the ratio of unwanted characters to the recommended characters
        Level - Beginner
    """

    unwanted = []
    for char in s:
        if char not in "abcdefghijklm":
            unwanted.append(char)

    return str(len(unwanted)) + "/" + str(len(s))


    