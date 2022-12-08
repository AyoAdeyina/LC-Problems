# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

# Example 1:

# Input: n = 2
# Output: [0,1,1]
# Explanation:
# 0 --> 0
# 1 --> 1
# 2 --> 10

# Type: Binary (Dynamic Programming)

class Solution(object):
    def countBits(self, n):
        # we use this to set the array to all zeros and use length of n plus one because that is how many we want to compute. 
        bit = [0] * (n+1)
        # This is keeping the highest power of two which is one in this case
        offset = 1

        # this is getting us the range from 1 all the way up into n value
        for i in range(1, n + 1):
            # Checking to see if we can double the offset
            if offset * 2 == i:
                offset = i
            # If offset equals i we can run this line of code that gets us the number of one bits in each 
            # intergers binary representation
            bit[i] = 1 + bit[i - offset]
        return bit