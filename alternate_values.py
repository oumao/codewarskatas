def alternate_values(n, first_value, second_value):
    arr = []
    while len(arr) < n:
        arr.append(first_value)
        arr.append(second_value)
        if len(arr) > n:
            arr.pop()
    return arr

print(alternate_values(5, True, False))