"""
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length

int k = removeDuplicates(nums); // Calls your implementation
"""

nums = [1, 1, 2]
expectedNums = len(nums) * ['_']
j = 0
for i in range(0,len(nums)):
    if nums[i] not in expectedNums:
        expectedNums[j] = nums[i]
        j += 1

print(expectedNums)

