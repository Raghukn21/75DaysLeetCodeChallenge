class Solution:
    def minimumLines(self, stockPrices: list[list[int]]) -> int:
        n = len(stockPrices)
        if n <= 2:
            return 1 if n == 2 else 0
        
        # 1. Sort points by day
        stockPrices.sort()
        
        lines = 1
        # 2. Compare slopes of consecutive segments
        for i in range(2, n):
            x1, y1 = stockPrices[i-2]
            x2, y2 = stockPrices[i-1]
            x3, y3 = stockPrices[i]
            
            # Cross-multiplication to compare slopes: 
            # (y2-y1)/(x2-x1) == (y3-y2)/(x3-x2)
            if (y2 - y1) * (x3 - x2) != (y3 - y2) * (x2 - x1):
                lines += 1
                
        return lines