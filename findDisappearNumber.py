# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
#
# Example:
#
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]

def findDisappearedNumbers(nums):
    hash_table = {}

    # Add each of the numbers to the hash table
    for num in nums:
        hash_table[num] = 1

    # Response array that would contain the missing numbers
    result = []

    # Iterate over the numbers from 1 to N and add all those
    # that don't appear in the hash table.
    for num in range(1, len(nums) + 1):
        if num not in hash_table:
            result.append(num)

    return result