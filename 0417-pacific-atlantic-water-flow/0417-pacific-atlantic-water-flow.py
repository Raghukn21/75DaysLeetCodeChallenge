class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        if not heights or not heights[0]:
            return []
            
        rows, cols = len(heights), len(heights[0])
        pacific_reachable = set()
        atlantic_reachable = set()
        
        def dfs(r, c, reachable_set, prev_height):
            # If out of bounds, already visited, or lower than the previous cell, stop
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                (r, c) in reachable_set or 
                heights[r][c] < prev_height):
                return
            
            # Mark this cell as reachable by this ocean
            reachable_set.add((r, c))
            
            # Traverse in all 4 directions
            dfs(r + 1, c, reachable_set, heights[r][c]) # Down
            dfs(r - 1, c, reachable_set, heights[r][c]) # Up
            dfs(r, c + 1, reachable_set, heights[r][c]) # Right
            dfs(r, c - 1, reachable_set, heights[r][c]) # Left

        # 1. Start DFS from Top and Bottom boundaries
        for c in range(cols):
            dfs(0, c, pacific_reachable, heights[0][c])          # Top row (Pacific)
            dfs(rows - 1, c, atlantic_reachable, heights[rows-1][c]) # Bottom row (Atlantic)
            
        # 2. Start DFS from Left and Right boundaries
        for r in range(rows):
            dfs(r, 0, pacific_reachable, heights[r][0])          # Left col (Pacific)
            dfs(r, cols - 1, atlantic_reachable, heights[r][cols-1]) # Right col (Atlantic)
            
        # 3. Find the intersection of cells reachable by both oceans
        return list(pacific_reachable.intersection(atlantic_reachable))