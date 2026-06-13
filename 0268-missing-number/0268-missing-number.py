class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        n = len(nums)
        # Calculate the expected sum of range [0, n]
        expected_sum = n * (n + 1) // 2
        # Calculate the actual sum of the array
        actual_sum = sum(nums)
        
        # The difference is the missing number
        return expected_sum - actual_sum