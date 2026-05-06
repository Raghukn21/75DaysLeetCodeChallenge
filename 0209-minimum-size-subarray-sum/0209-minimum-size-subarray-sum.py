class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        n = len(nums)
        min_length = float('inf')
        current_sum = 0
        left = 0
        
        # 'right' expands the window
        for right in range(n):
            current_sum += nums[right]
            
            # While the sum is sufficient, try to shrink the window from the left
            while current_sum >= target:
                # Update the minimum length found so far
                min_length = min(min_length, right - left + 1)
                
                # Shrink the window and update the sum
                current_sum -= nums[left]
                left += 1
                
        # If min_length was never updated, return 0
        return min_length if min_length != float('inf') else 0