# Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming weight).

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type. In this case, the input will be given as a signed integer type. It should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3, the input represents the signed integer. -3.

# Example 1:

# Input: n = 00000000000000000000000000001011
# Output: 3
# Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

# Type: Binary


class Solution(object):
    def hammingWeight(self, n):
        # sol is used to declare the total number of ones we will have in the problem
        sol = 0

        # using the while loop to continue to count the ones within the problem
        while n:
            # we use the n % 2 to tell whether or not the ones place in the problem will return one or zero. 
            # If it  is a one we want to increment by 1 and if it is a zero we don't want to increment at all.
            sol += n % 2
            # we want to shift everything to the right by one we do this using bit manipulation, setting n equal to itself and shifting it by one.
            n = n >> 1
        return sol
