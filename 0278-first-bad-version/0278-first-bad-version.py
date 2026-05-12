# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        
        while left < right:
            # Use (left + right) // 2 or the overflow-safe way:
            mid = left + (right - left) // 2
            
            if isBadVersion(mid):
                # This could be the first bad version, 
                # but let's check the left side to be sure.
                right = mid
            else:
                # This is definitely a good version, 
                # so the first bad one must be further right.
                left = mid + 1
                
        # When left == right, we've found the boundary.
        return left