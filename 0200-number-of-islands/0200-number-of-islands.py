class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        island_count = 0
        
        def dfs(r, c):
            # Base case: if out of bounds or at a water cell ('0'), stop DFS
            if r < 0 or r >= rows or c < 0 or c >= cols or grid[r][c] == '0':
                return
            
            # Mark the current land cell as visited by turning it into water
            grid[r][c] = '0'
            
            # Explore all 4 adjacent directions (Up, Down, Left, Right)
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        # Scan every cell in the 2D grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # Found a new island! Trigger DFS to sink it entirely
                    dfs(r, c)
                    island_count += 1
                    
        return island_count