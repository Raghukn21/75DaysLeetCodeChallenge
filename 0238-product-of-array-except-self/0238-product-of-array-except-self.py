class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        n = len(nums)
        res = [1] * n
        
        # Step 1: Prefix Products
        prefix = 1
        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]
            
        # Step 2: Suffix Products
        suffix = 1
        for i in range(n - 1, -1, -1):
            res[i] *= suffix
            suffix *= nums[i]
            
        return res
        