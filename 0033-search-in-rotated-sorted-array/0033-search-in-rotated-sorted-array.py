class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            
            # Determine which side is sorted
            if nums[low] <= nums[mid]:
                # Left side is sorted
                if nums[low] <= target < nums[mid]:
                    high = mid - 1  # Target is in the sorted left half
                else:
                    low = mid + 1   # Target must be in the right half
            else:
                # Right side is sorted
                if nums[mid] < target <= nums[high]:
                    low = mid + 1   # Target is in the sorted right half
                else:
                    high = mid - 1  # Target must be in the left half
                    
        return -1