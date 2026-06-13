import math
from collections import defaultdict

class Solution:
    def maxPoints(self, points: list[list[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        overall_max = 0
        
        for i in range(n):
            slopes = defaultdict(int)
            duplicate = 1  # The point i itself
            current_max = 0
            
            for j in range(n):
                if i == j:
                    continue
                    
                dx = points[j][0] - points[i][0]
                dy = points[j][1] - points[i][1]
                
                # Handle duplicate points
                if dx == 0 and dy == 0:
                    duplicate += 1
                    continue
                
                # Simplify the slope using GCD
                common = math.gcd(dx, dy)
                slope = (dx // common, dy // common)
                
                slopes[slope] += 1
                current_max = max(current_max, slopes[slope])
            
            # Max points for this anchor is (max points found with a slope) + duplicates
            overall_max = max(overall_max, current_max + duplicate)
            
        return overall_max