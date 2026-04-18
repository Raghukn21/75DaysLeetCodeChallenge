class Solution:
    def hasPathSum(self, root, targetSum):
        if root is None:
            return False
        
        # If it's a leaf node
        if root.left is None and root.right is None:
            return targetSum == root.val
        
        # Recurse on left and right
        return (self.hasPathSum(root.left, targetSum - root.val) or
                self.hasPathSum(root.right, targetSum - root.val))
