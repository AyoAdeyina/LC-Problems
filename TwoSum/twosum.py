# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.

# Use a Hashmap (we use the hashmap in this situation to map each value to the index of each value)

from ast import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # this will give us the value and index of the array
        lastMap = {}

        for a, b in enumerate(nums):
            newVal = target - b
            if newVal in lastMap:
                return [lastMap[newVal], a]
            lastMap[b] = a
        return

# Problem type = Array
# Note: enumerate() method adds a counter to an iterable and returns it in a form of enumerating object