# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root: TreeNode) -> list[int]:
        result = []
        
        def dfs(node):
            if not node:
                return
            # 1. Process Root
            result.append(node.val)
            # 2. Process Left
            dfs(node.left)
            # 3. Process Right
            dfs(node.right)
            
        dfs(root)
        return result