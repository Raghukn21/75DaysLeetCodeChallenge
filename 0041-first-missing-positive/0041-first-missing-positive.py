class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        
        # Place each number in its correct spot if possible
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target index
                target_idx = nums[i] - 1
                nums[i], nums[target_idx] = nums[target_idx], nums[i]
        
        # Find the first index where the value is incorrect
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # If all numbers 1 to n are present, the answer is n + 1
        return n + 1