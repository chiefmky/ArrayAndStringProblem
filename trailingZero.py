'''
For an integer N find the number of trailing zeroes in N!.

Example 1:

Input:
N = 5
Output:
1
Explanation:
5! = 120 so the number of trailing zero is 1.
Example 2:

Input:
N = 4
Output:
0
Explanation:
4! = 24 so the number of trailing zero is 0.
'''

def trailingZeroes(self, N):
    count = 0
    while (N != 0):
        N = N // 5
        count += N
    return count