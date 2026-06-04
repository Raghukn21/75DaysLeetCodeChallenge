class Solution:
    def rob(self, nums: list[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # prev2 represents max money up to house i-2
        # prev1 represents max money up to house i-1
        prev2, prev1 = 0, 0
        
        for num in nums:
            # At each step, calculate the max money possible
            # Either we rob this house (num + prev2) or skip it (prev1)
            current = max(prev1, prev2 + num)
            prev2 = prev1
            prev1 = current
            
        return prev1