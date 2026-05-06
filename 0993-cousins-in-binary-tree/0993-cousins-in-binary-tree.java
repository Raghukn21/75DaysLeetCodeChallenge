import java.util.*;

class Solution {
    public boolean isCousins(TreeNode root, int x, int y) {
        if (root == null) return false;

        Queue<TreeNode> queue = new LinkedList<>();
        queue.add(root);

        while (!queue.isEmpty()) {
            int size = queue.size();
            boolean foundX = false;
            boolean foundY = false;

            for (int i = 0; i < size; i++) {
                TreeNode parent = queue.poll();

                // Check children to ensure x and y are not siblings
                if (parent.left != null && parent.right != null) {
                    if ((parent.left.val == x && parent.right.val == y) ||
                        (parent.left.val == y && parent.right.val == x)) {
                        return false; // They are siblings, not cousins
                    }
                }

                // Standard BFS traversal
                if (parent.left != null) {
                    if (parent.left.val == x) foundX = true;
                    if (parent.left.val == y) foundY = true;
                    queue.add(parent.left);
                }
                
                if (parent.right != null) {
                    if (parent.right.val == x) foundX = true;
                    if (parent.right.val == y) foundY = true;
                    queue.add(parent.right);
                }
            }

            // If both are found at the same level (and not siblings), they are cousins
            if (foundX && foundY) return true;
            
            // If only one is found at this level, they can't be cousins
            if (foundX || foundY) return false;
        }

        return false;
    }
}