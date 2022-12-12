# Reverse bits of a given 32 bits unsigned integer.

# Note:

# Note that in some languages, such as Java, there is no unsigned integer type. In this case, both input and output will be given as a signed integer type. 
# They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
# In Java, the compiler represents the signed integers using 2's complement notation. 
# Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.

# Example 1:

# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, 
# so return 964176192 which its binary representation is 00111001011110000010100101000000.

# Type: Bit manipulation operations

class Solution:
    def reverseBits(self, n):
        # This result variavble is declaring all 32 bits being initialized at zero 
        result = 0 
        # We want to go through every single bit in the input i
        for i in range(32):
            # Take n and shift it all the way to the right with i, 
            # then in n we will have the result bit we are looking for and it would be in the ones spot
            # to get the result of the ones spot we & it with one 
            # The bit would be either one or zero 
            # We will get the first bit from n and put it in the 31 spot of the result
            bit = (n >> i) & 1
            # We start at the largest bit and shift down from there
            # We shift our bit to right by 31 minus i
            # We get the bit in index one from n and putting it in index 30 in the output
            result = result | (bit << (31 - i))
        return result
