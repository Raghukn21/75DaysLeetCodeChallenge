# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None
            
        # Dictionary to save old_node -> new_clone_node
        old_to_new = {}
        
        def dfs(curr_node):
            # If we already cloned this node, return the existing clone
            if curr_node in old_to_new:
                return old_to_new[curr_node]
                
            # Create a deep copy of the current node (without neighbors for now)
            clone = Node(curr_node.val)
            old_to_new[curr_node] = clone
            
            # Recursively clone and append all neighbors
            for neighbor in curr_node.neighbors:
                clone.neighbors.append(dfs(neighbor))
                
            return clone
            
        return dfs(node)