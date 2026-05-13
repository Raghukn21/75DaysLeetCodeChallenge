class Solution:
    def findPeakElement(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            # Compare middle element with its right neighbor
            if nums[mid] < nums[mid + 1]:
                # We are on an upward slope. 
                # The peak must be to the right (excluding mid)
                left = mid + 1
            else:
                # We are on a downward slope or at a potential peak.
                # The peak is to the left (including mid)
                right = mid
                
        # When left == right, we have narrowed down to a peak element
        return left