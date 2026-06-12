class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        def dfs(r, c):
            # Base case: out of bounds or empty cell
            if not (0 <= r < rows and 0 <= c < cols) or grid[r][c] == 0:
                return 0
            
            # Store original gold and mark as visited
            temp = grid[r][c]
            grid[r][c] = 0
            
            # Explore 4 directions
            max_gold = 0
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                max_gold = max(max_gold, dfs(r + dr, c + dc))
            
            # Backtrack: restore the cell value
            grid[r][c] = temp
            
            return temp + max_gold

        max_total = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] != 0:
                    max_total = max(max_total, dfs(r, c))
                    
        return max_total