# Given two integers a and b, return the sum of the two integers without using the operators + and -.

# Example 1:

# Input: a = 1, b = 2
# Output: 3


class Solution(object):
    def getSum(self, a, b):
        # Until the carry value ends up being 0, b is what we use for the carry in this case
        while (b != 0):
            # We create a tmp variable and set it equal to (a & b) << 1, this (<< 1) means we bit shift it to the left by one
            # This checks for the carry
            tmp = (a & b) << 1
            # We are setting a = a XOR b (a ^ b), we do this so we can add each number bit by bit 
            # (this does not take care of the carry)
            a = a ^ b
            # We set b equal to tmp so that we use the orginal value of a and not the new value of a
            b = tmp
        return a