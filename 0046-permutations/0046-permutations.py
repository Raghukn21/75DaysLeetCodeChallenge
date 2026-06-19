class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        results = []
        
        def backtrack(current_path, remaining_nums):
            # Base case: no numbers left to add
            if not remaining_nums:
                results.append(current_path)
                return
            
            # Recursive step: try every remaining number
            for i in range(len(remaining_nums)):
                # Choose the number at i
                # Recurse with new path and remaining list excluding the chosen number
                backtrack(current_path + [remaining_nums[i]], 
                          remaining_nums[:i] + remaining_nums[i+1:])
        
        backtrack([], nums)
        return results