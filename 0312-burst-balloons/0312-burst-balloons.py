class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # Add boundaries of 1 to handle the multiplication at the edges
        nums = [1] + nums + [1]
        n = len(nums)
        # dp[i][j] stores the max coins in the interval (i, j)
        dp = [[0] * n for _ in range(n)]
        
        # length is the length of the interval
        for length in range(2, n):
            for i in range(n - length):
                j = i + length
                # k is the last balloon to burst in the interval (i, j)
                for k in range(i + 1, j):
                    dp[i][j] = max(dp[i][j], 
                                   dp[i][k] + dp[k][j] + nums[i] * nums[k] * nums[j])
                    
        return dp[0][n - 1]