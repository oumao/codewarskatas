def max_min(arr):
    """
    Printing maximum numbers in an array in descending while the minimum numbers in 
    an ascending number
    i.e
    Input:  arr = [1,4, 3, 7, 6]
    Output: arr = [7, 1, 6, 3, 4]
    """
    large_idx = len(arr)-1
    small_idx = 0
    n = len(arr)
    temp = n*[None]

    flag = True

    for i in range(n):
        if flag is True:
            temp[i] = arr[large_idx]
            large_idx -= 1
        else:
            temp[i] = arr[small_idx]
            small_idx += 1
        flag = not flag

    for i in range(n):
        arr[i] = temp[i]

    return arr


print(max_min([1, 2, 3, 4, 5, 6]))


    