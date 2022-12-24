"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they
add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

"""

nums_ = [2,5,5,11]
target_ = 10


def two_s(nums, target):
    i = 0
    for i in range(0, len(nums), 1):
        to_match = target- nums[i]
        if to_match in nums:
            j = nums.index(to_match)
            if i!= j:
                return [i,j]

    return []


    # for i in range(0, len(nums) , 1):
    #     for j in range(1, len(nums) , 1):
    #         if nums[i]+ nums[j] == target and i != j:
    #             return [i,j]


print(two_s(nums_, target_))
