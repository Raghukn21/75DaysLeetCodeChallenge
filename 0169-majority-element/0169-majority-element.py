class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        candidate = None
        count = 0
        
        for num in nums:
            # If count is 0, we have no current "leader", so take the current num
            if count == 0:
                candidate = num
            
            # If the current num is the leader, increment; otherwise, decrement
            count += (1 if num == candidate else -1)
            
        return candidate