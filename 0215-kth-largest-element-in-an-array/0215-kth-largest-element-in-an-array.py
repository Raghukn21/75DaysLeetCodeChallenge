import heapq

# 1. Make sure you define the Solution class exactly like this
class Solution:
    # 2. Make sure the function is indented inside the class
    def findKthLargest(self, nums: list[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
                
        return min_heap[0]