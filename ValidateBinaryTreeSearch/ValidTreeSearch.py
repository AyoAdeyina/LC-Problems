# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# The left subtree of a node contains only nodes with keys less than the node's key.
# The right subtree of a node contains only nodes with keys greater than the node's key.
# Both the left and right subtrees must also be binary search trees.

# Example 1:


# Input: root = [2,1,3]
# Output: true

# Use Recursive DFS

class Solution(object):
    def isValidBST(self, root):

        # Create a helper function nested inside of the original function 
        def valid (node, left, right):
            # If it reaches a null node it should return True
            if not node:
                return True
            # Checking to see if the node is less then the right boundry and greater than the left boundry 
            # and if not return false
            if not (node.val < right and node.val > left):
                return False

            # Making our recursive call
            # Make sure the left subtree of node is valid so pass node.left, the boundry can be left since we are going left
            # and we are going to update the right value to the nodes boundry
            return (valid(node.left, left, node.val) and
            # Also want to makre sure the right subtree is valid, so the left boundry is update (node.val)
            #  and the right boundry is going to stay the same
            valid(node.right, node.val, right))
        # Calling the function we defined (valid) and pass in root while setting the left boundry to -infinity
        #  and the right boundry to infinity because the root could be anything
        return valid(root, float("-inf"), float("inf"))

class Solution(object):
    def isValidBST(self, root):

        def valid (node, left, right):
            if not node:
                return True

            if not (node.val < right and node.val > left):
                return False

            return (valid(node.left, left, node.val) and
            valid(node.right, node.val, right))
            
        return valid(root, float("-inf"), float("inf"))
