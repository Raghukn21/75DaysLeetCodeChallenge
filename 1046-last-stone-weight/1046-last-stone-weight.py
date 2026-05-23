import heapq

class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        # Convert all weights to negative to simulate a Max-Heap
        max_heap = [-s for s in stones]
        heapq.heapify(max_heap)
        
        # Keep smashing until 0 or 1 stone remains
        while len(max_heap) > 1:
            # Extract the two heaviest stones (invert back to positive)
            stone1 = -heapq.heappop(max_heap)
            stone2 = -heapq.heappop(max_heap)
            
            # If they aren't equal, push the remaining fragment back
            if stone1 != stone2:
                remaining_weight = stone1 - stone2
                heapq.heappush(max_heap, -remaining_weight)
                
        # If the heap is empty, return 0; otherwise, return the last stone's true value
        return -max_heap[0] if max_heap else 0