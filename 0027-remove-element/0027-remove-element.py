class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0  # Write pointer
        
        for i in range(len(nums)):
            # If the current element is not the target value
            if nums[i] != val:
                # Place it at the 'k' position and increment k
                nums[k] = nums[i]
                k += 1
                
        # 'k' is now the count of elements not equal to val
        return k