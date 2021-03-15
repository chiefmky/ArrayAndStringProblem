# Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.
#
# Example 1:
# Input: [1,0,1,1,0]
# Output: 4
# Explanation: Flip the first zero will get the the maximum number of consecutive 1s.
#     After flipping, the maximum number of consecutive 1s is 4.

def findMaxConsecutiveOnes(nums):
    left = 0
    right = 0
    longest_count = 0
    zero_count = 0
    z_ind = 0

    while left < len(nums) and right < len(nums):
        if nums[right] == 0 and zero_count < 1:
            zero_count += 1
            z_ind = right
        elif nums[right] == 0 and zero_count == 1:
            longest_count = max(longest_count, len(nums[left:right]))
            zero_count = 1
            left = z_ind + 1
            z_ind = right
        longest_count = max(longest_count, len(nums[left:(right + 1)]))
        right += 1
    return longest_count

'''Optimal version'''
def findMaxConsecutiveOnes1(nums):
    longest_sequence = 0
    left, right = 0, 0
    num_zeroes = 0

    while right < len(nums):  # while our window is in bounds
        if nums[right] == 0:  # add the right most element into our window
            num_zeroes += 1

        while num_zeroes == 2:  # if our window is invalid, contract our window
            if nums[left] == 0:
                num_zeroes -= 1
            left += 1

        longest_sequence = max(longest_sequence, right - left + 1)  # update our longest sequence answer
        right += 1  # expand our window

    return longest_sequence