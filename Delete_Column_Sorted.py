def delete_column(strs: list[str]) -> int:
    """
    Publisher: LeetCode - Problem 944

    You are given an array of n strings strs, all of the same length.
    The strings can be arranged such that there is one on each line, making a grid. For example, strs = ["abc", "bce", "cae"] can be arranged as:

    abc
    bce
    cae
    You want to delete the columns that are not sorted lexicographically. In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e') are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.

    Return the number of columns that you will delete.

    
    """

    count = 0 # Initialize count to zero
    len_str = len(strs[0]) # Size of each string in the list
    len_lst = len(strs) # Size of the list


    # Iterating over each character in the string columnwise
    for j in range(len_str):

        # Iterating over each string starting from the second comparing with the first
        for i in range(1, len_lst):

            # when column is sorte no searching further
            if strs[i][j] < strs[i-1][j]:
                count += 1
                break

    return count



print(delete_column(["cba","daf","ghi"]))