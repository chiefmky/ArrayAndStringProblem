# Given integer array nums, return the third maximum number in this array.
# If the third maximum does not exist, return the maximum number.
#
# Example
# 1:
#
# Input: nums = [3, 2, 1]
# Output: 1
# Explanation: The third maximum is 1.
# Example
# 2:
#
# Input: nums = [1, 2]
# Output: 2
# Explanation: The third maximum does not exist, so the maximum(2) is returned instead.
'''O(n) time'''
'''O(n) space'''
def thirdMax(nums):
    nums = set(nums)

    if len(nums) <= 2:
        return max(nums)

    newArr = []

    for num in nums:
        newArr.append(num)
    i = 0
    while i < 3:
        ans = max(newArr)
        idx = newArr.index(ans)
        newArr.pop(idx)
        i += 1

    return ans

'''Optimal solution'''
'''O(n) time'''
'''O(1) space'''
def thirdMax(nums):
    maximums = set()
    for num in nums:
        maximums.add(num)
        if len(maximums) > 3:
            maximums.remove(min(maximums))
    if len(maximums) == 3:
        return min(maximums)
    return max(maximums)