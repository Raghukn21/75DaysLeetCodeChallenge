class Solution:
    def calculateMinimumHP(self, dungeon: list[list[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        # dp[i][j] stores the min health needed to enter room (i, j)
        dp = [[0] * n for _ in range(m)]
        
        # Base case: The bottom-right room
        dp[m-1][n-1] = max(1, 1 - dungeon[m-1][n-1])
        
        # Fill the last column
        for i in range(m - 2, -1, -1):
            dp[i][n-1] = max(1, dp[i+1][n-1] - dungeon[i][n-1])
            
        # Fill the last row
        for j in range(n - 2, -1, -1):
            dp[m-1][j] = max(1, dp[m-1][j+1] - dungeon[m-1][j])
            
        # Fill the rest of the table
        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                min_health_on_exit = min(dp[i+1][j], dp[i][j+1])
                dp[i][j] = max(1, min_health_on_exit - dungeon[i][j])
                
        return dp[0][0]