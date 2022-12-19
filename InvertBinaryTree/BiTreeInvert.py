# Given the root of a binary tree, invert the tree, and return its root.

# Example 1:


# Input: root = [4,2,7,1,3,6,9]
# Output: [4,7,2,9,6,3,1]

class Solution(object):
    def invertTree(self, root):
        # Check the base case first, so if the root is null return none
        if not root:
            return None
        
        # Swap the children next

        # Store the root.left value in a temporary variable (tvar)
        tvar = root.left
        # Replacing the root.left variable with the root.right variable
        root.left = root.right
        # Replacing the root.right variable with the root.left variable which is stored in them temporary variable (tvar)
        root.right = tvar

        # Now recursively invert the sub-trees
        
        # By using self.invertTree we are making a recursive call to the function we are inside
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root