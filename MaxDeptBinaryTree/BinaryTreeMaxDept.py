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


# Type: Iteratively DFS - will need to use a stack data structure
# using pre-order DFS with this stack 

class Solution(object):
    def maxDepth(self, root):
        # We add the root which is the node and 1 which is the depth
        stack = [[root, 1]]
        # We set our result = 0 so if we do have a null root node the loop will execute, will pop the stack but then the 
        # if statement won't execute so then the result will stay zero
        # And if the result is non null we will end up updating the result with the if statement
        result = 0
        # We create while loop to say "while the stack is non-empty"
        while stack:
            # We are going to pop the node and depth from the stack
            node, depth = stack.pop()
        # We are stating here if the node is non null
        # This if statement is preventing us from using any null nodes
            if node:
                # We update the result by setting it to the max of itself and the depth of the node we just popped
                result = max(result, depth)
                # We are appending the left node and append it with the depth of the node we just popped plus one
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        return result
