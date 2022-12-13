# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

# Example 1:

# Input: nums = [3,4,5,1,2]
# Output: 1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.

# Type: Binary Search Algorithm

class Solution(object):
    def findMin(self, nums):

        # Setting the variable result to nums[0] which would put us at the left most number of the array
        result = nums[0]
        # We have our two pointers lp will be all the way at the left at index 0 and 
        # right is going to be all the way to right most index using len(nums) - 1
        lp, rp = 0, len(nums) - 1

        # Keep runing the binary search while our pointers are at a valid position while lp <= rp
        while lp <= rp:
            # if the value at the lp is less than the value at the rp
            if nums[lp] < nums[rp]:
                # We can update the result by setting the result to the minimum of itself and the left most value 
                # of the sorted portion of the array
                result = min(result, nums[lp])
                # Then we can break out of this while loop
                break
            
            # If the array is not sorted this is what will need to do to start the binary search
            # Take the mid pointer and add the lp + rp  and use interger division by 2
            mid = (lp +rp) // 2
            # We then update the result setting the result equal to the minimum of itself and 
            # the value at the mid pointer in the array
            result = min(result, nums[mid])
            # To tell if the mid value is apart of the left sorted portion, check to see if the value
            # of the mid index is greater than or equal to the left index
            if nums[mid] >= nums[lp]:
                # Searches the right pointer portion
                lp = mid + 1
            else:
                # Searches the left pointer portion
                rp = mid - 1
        return result
