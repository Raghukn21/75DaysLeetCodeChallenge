class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        buy1 = float('inf')
        profit1 = 0
        buy2 = float('inf')
        profit2 = 0
        
        for price in prices:
            # First transaction
            buy1 = min(buy1, price)
            profit1 = max(profit1, price - buy1)
            
            # Second transaction (reinvesting profit1)
            # The "effective" cost of the second stock is price - profit1
            buy2 = min(buy2, price - profit1)
            profit2 = max(profit2, price - buy2)
            
        return profit2