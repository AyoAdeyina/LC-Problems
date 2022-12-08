# You are climbing a staircase. It takes n steps to reach the top.

# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?


# Example 1:

# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps

class Solution(object):
    def climbStairs(self, n):

        # We have two variables one and two which are intialized as 1
        one, two = 1, 1

        # We are going to loop through N - 1 times and we are going to continuously update one and two 
        for i in range (n-1):
            # Storing one in a temporary variable before we actually update it
            sub = one 
            # One is going to be updated by adding one plus two because we are continuously adding the two previous values
            # and getting a new result
            one = one + two
            # So we set two to one by setting it to the temporary variable which is "sub"
            two = sub
        # We return one because we want to return whatever one land on in the set
        return one