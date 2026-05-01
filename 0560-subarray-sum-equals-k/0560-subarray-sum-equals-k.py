class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # Dictionary to store (prefix_sum : count)
        prefix_sums = {0: 1}
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            
            # Check if (current_sum - k) exists in our map
            if (current_sum - k) in prefix_sums:
                count += prefix_sums[current_sum - k]
            
            # Update the map with the current prefix sum
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return count