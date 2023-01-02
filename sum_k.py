def sum_k(num, K: int) -> int:

    """
        Function to return maximum S such that there exists i < j with A[i] +A[j] = S and S < K
        O(n*n)
    """

    # Initialize maximum sum
    max_sum = 0

    size = len(num)

    for i in range(size):
        for j in range(i+1, size):

            # Check if the sum of two integers in the array are less than K
            if num[i] + num[j] < K:
                max_sum = max(max_sum, num[i] + num[j])
    
    return max_sum


print(sum_k([2, 4, 3, 5, 7], 10))
