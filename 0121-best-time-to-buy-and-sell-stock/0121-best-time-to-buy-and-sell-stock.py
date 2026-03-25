class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # We start with the first price as our minimum
        min_price = float('inf')
        max_profit = 0
        
        for price in prices:
            # Update the lowest price found so far
            if price < min_price:
                min_price = price
            # Check if selling at the current price gives a better profit
            elif price - min_price > max_profit:
                max_profit = price - min_price
                
        return max_profit
        