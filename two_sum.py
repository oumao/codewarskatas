def two_sum(nums, target, dict={}):
    for key, value in enumerate(nums):
        if target - value in dict:
            return [dict[target - value], key]
        dict[value] = key 


print(two_sum([2,2,5,6], 11))