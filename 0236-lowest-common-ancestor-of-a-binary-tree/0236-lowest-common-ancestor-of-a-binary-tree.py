# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Base Case: If we reach the end of a branch or find p or q
        if not root or root == p or root == q:
            return root
        
        # Look for p and q in the left and right subtrees
        left_search = self.lowestCommonAncestor(root.left, p, q)
        right_search = self.lowestCommonAncestor(root.right, p, q)
        
        # If p is found on one side and q on the other, this node is their LCA
        if left_search and right_search:
            return root
        
        # Otherwise, return the non-null result (bubble up the found node)
        return left_search if left_search else right_search