# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        self.cameras = 0
        
        # 0: Needs Monitoring, 1: Has Camera, 2: Covered
        def dfs(node):
            if not node:
                return 2  # Null nodes are covered
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            # If any child needs monitoring, place a camera here
            if left == 0 or right == 0:
                self.cameras += 1
                return 1
            
            # If any child has a camera, this node is covered
            if left == 1 or right == 1:
                return 2
            
            # Otherwise, this node needs monitoring from its parent
            return 0
        
        # Final check for the root
        if dfs(root) == 0:
            self.cameras += 1
            
        return self.cameras