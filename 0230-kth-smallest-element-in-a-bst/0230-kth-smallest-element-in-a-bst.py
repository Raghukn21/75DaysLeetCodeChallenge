class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.result = None
        
        def inorder(node):
            if not node or self.result is not None:
                return
            
            # 1. Go Left
            inorder(node.left)
            
            # 2. Process Current Node
            self.k -= 1
            if self.k == 0:
                self.result = node.val
                return
            
            # 3. Go Right
            inorder(node.right)
            
        inorder(root)
        return self.result