# Definition for a binary tree node (Do not define this if the platform provides it)
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string."""
        def preorder(node):
            if not node:
                return ["#"]
            return [str(node.val)] + preorder(node.left) + preorder(node.right)
        return ",".join(preorder(root))

    def deserialize(self, data):
        """Decodes your encoded data to tree."""
        nodes = iter(data.split(","))
        
        def build():
            val = next(nodes)
            if val == "#":
                return None
            node = TreeNode(int(val))
            node.left = build()
            node.right = build()
            return node
            
        return build()