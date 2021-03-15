'''
Given an array of size N-1 such that it can only contain distinct integers in the range of 1 to N.
Find the missing element.

Example 1:

Input:
N = 5
A[] = {1,2,3,5}
Output: 4
Example 2:

Input:
N = 10
A[] = {1,2,3,4,5,6,7,8,10}
Output: 9
'''

def MissingNumber(array,n):
    # code here
    arrSet = set(array)
    for num in arrSet:
        numSet = num
        if num == 1:
            while numSet+1 in arrSet:
                numSet += 1
            return numSet+1
        else:
            return 1

