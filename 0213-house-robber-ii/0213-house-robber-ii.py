class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def rob_linear(houses):
            prev2, prev1 = 0, 0
            for money in houses:
                current = max(prev1, prev2 + money)
                prev2 = prev1
                prev1 = current
            return prev1

        # The circular constraint requires splitting the problem:
        # Either exclude the last house or exclude the first house.
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))