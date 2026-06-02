class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        # We start at index 0 or 1, so the cost to reach them is their own cost
        prev2 = cost[0]
        prev1 = cost[1]
        
        # Calculate min cost for each step from 2 to n-1
        for i in range(2, n):
            current = cost[i] + min(prev1, prev2)
            prev2 = prev1
            prev1 = current
            
        # The top is reached from either the last or second-to-last step
        return min(prev1, prev2)