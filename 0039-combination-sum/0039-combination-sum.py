class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        results = []
        
        def backtrack(remaining, start_index, current_combination):
            # Base case: target met
            if remaining == 0:
                results.append(list(current_combination))
                return
            # Base case: target exceeded
            if remaining < 0:
                return
            
            for i in range(start_index, len(candidates)):
                # Include candidate
                current_combination.append(candidates[i])
                # Recursion: pass 'i' as start_index to allow reuse of the same element
                backtrack(remaining - candidates[i], i, current_combination)
                # Backtrack: remove candidate before the next iteration
                current_combination.pop()
        
        backtrack(target, 0, [])
        return results