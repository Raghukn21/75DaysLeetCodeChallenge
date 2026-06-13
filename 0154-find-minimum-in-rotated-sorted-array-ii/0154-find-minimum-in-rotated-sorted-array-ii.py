class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            if nums[mid] > nums[right]:
                # The minimum must be in the right half
                left = mid + 1
            elif nums[mid] < nums[right]:
                # The minimum is in the left half (including mid)
                right = mid
            else:
                # When nums[mid] == nums[right], we can't be sure;
                # shrink the search space by one
                right -= 1
                
        return nums[left]