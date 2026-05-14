import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        # Range of possible speeds
        left = 1
        right = max(piles)
        
        def can_finish(k: int) -> bool:
            total_hours = 0
            for pile in piles:
                # Calculate hours needed for this pile at speed k
                # (Equivalent to math.ceil(pile / k))
                total_hours += (pile + k - 1) // k
            return total_hours <= h

        # Binary search for the minimum k
        while left < right:
            mid = left + (right - left) // 2
            
            if can_finish(mid):
                # If she can finish, try a smaller speed
                right = mid
            else:
                # If she can't finish, she needs to eat faster
                left = mid + 1
        
        return left