
# Swapping Function
def bubble_sort(arr):
    """Function to sort array by swapping - O(n*n) """
    ln = len(arr)
    for i in range(1, ln):
        for j in range(0, ln-i):
            if(arr[j] > arr[j+1]):
                arr[j], arr[j+1] = arr[j+1], arr[j]
    

if __name__ == '__main__':
    nums = [3, 4, 2, 9, 8, 6, 1, 7]
    bubble_sort(nums)
    print(nums)
