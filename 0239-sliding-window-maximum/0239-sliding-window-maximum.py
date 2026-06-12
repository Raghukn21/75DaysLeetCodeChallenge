from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        # Using a deque to store indices of potential maximums
        # The deque will maintain elements in decreasing order
        dq = deque()
        res = []
        
        for i, n in enumerate(nums):
            # Remove indices that are out of the current window
            if dq and dq[0] < i - k + 1:
                dq.popleft()
                
            # Maintain decreasing order: remove smaller elements from the back
            while dq and nums[dq[-1]] < n:
                dq.pop()
                
            dq.append(i)
            
            # The first element is always the maximum for the current window
            if i >= k - 1:
                res.append(nums[dq[0]])
                
        return res