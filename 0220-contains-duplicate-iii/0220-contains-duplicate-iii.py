from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: list[int], indexDiff: int, valueDiff: int) -> bool:
        # SortedList stores elements in the current sliding window of size indexDiff
        window = SortedList()
        
        for i in range(len(nums)):
            # If window exceeds size, remove the element that is out of indexDiff range
            if i > indexDiff:
                window.remove(nums[i - indexDiff - 1])
            
            # Find the smallest value >= nums[i] - valueDiff
            val_to_find = nums[i] - valueDiff
            idx = window.bisect_left(val_to_find)
            
            # Check if such value exists and satisfies the valueDiff condition
            if idx < len(window) and window[idx] <= nums[i] + valueDiff:
                return True
            
            # Add current element to the window
            window.add(nums[i])
            
        return False