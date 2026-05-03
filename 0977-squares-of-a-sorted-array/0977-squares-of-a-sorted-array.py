class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        n = len(nums)
        # Result array to store squared values
        result = [0] * n
        
        left = 0
        right = n - 1
        # We fill the result array from back to front
        pos = n - 1
        
        while left <= right:
            left_square = nums[left] ** 2
            right_square = nums[right] ** 2
            
            if left_square > right_square:
                result[pos] = left_square
                left += 1
            else:
                result[pos] = right_square
                right -= 1
            
            pos -= 1
            
        return result