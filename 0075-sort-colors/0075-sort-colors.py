class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        low = 0          # Pointer for the next position of 0
        mid = 0          # Current element being inspected
        high = len(nums) - 1  # Pointer for the next position of 2
        
        while mid <= high:
            if nums[mid] == 0:
                # Found a Red (0), swap it to the front
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Found a White (1), it's already in the "middle"
                mid += 1
            else:
                # Found a Blue (2), swap it to the end
                nums[high], nums[mid] = nums[mid], nums[high]
                # Do NOT increment mid here, because the swapped value 
                # from high needs to be inspected.
                high -= 1