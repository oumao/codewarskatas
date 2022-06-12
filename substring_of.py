def in_array(arr1, arr2):
    sorts = set()
    for word in arr2:
        for st in arr1:
            if st in word:
                sorts.add(st)
    return sorted(list(sorts))