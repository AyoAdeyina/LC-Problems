# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

# Example 1:

# Input: root = [3,9,20,null,null,15,7]
# Output: 3

# Time: O(n)

# Type: Recursive Depth First Search

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        # Start with base case: so if root is null, then we return 0 that is the max depth
        if not root:
            return 0
        # Otherwise we are going to rertun 1 + the maxDepth on the left and right subtree
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
        # So we are just taking the result of both of these function calls figuring out what the max subtree depth of both of the subtrees
        # We are adding one to it because we know that the current root node we are traversing is definitely not null