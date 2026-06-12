class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        
        def get_max_gain(node):
            if not node:
                return 0
            
            # Recursively get max gain from left and right children
            # If gain is negative, we don't include it (use 0)
            left_gain = max(get_max_gain(node.left), 0)
            right_gain = max(get_max_gain(node.right), 0)
            
            # Path sum through the current node
            current_path_sum = node.val + left_gain + right_gain
            
            # Update global max
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return max gain the node can provide to its parent
            return node.val + max(left_gain, right_gain)
        
        get_max_gain(root)
        return self.max_sum