# Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of 
# all the values of the nodes in the tree.

# Example 1:


# Input: root = [3,1,4,null,2], k = 1
# Output: 1


class Solution(object):
    def kthSmallest(self, root, k):
        def newlst(root):
            if not root: 
                return []
            return newlst(root.left) + [root.val] + newlst(root.right)

        return newlst(root)[k-1]