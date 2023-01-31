def max_sum_sub_arrays(arr):
    """
    Using Kadane's Algorithm to solve max sum of subarrays
    """

    # Declare max_sum and current_sum
    max_sum = -1e8
    
    n = len(arr)

    for i in range(n):
        curr_sum = 0
        for j in range(i, n):
            curr_sum += arr[j]

            if curr_sum > max_sum:
                max_sum = curr_sum
            
    return max_sum

print(max_sum_sub_arrays([1, 2, 3]))
    
