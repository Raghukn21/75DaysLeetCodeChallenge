import heapq

class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.heap = nums
        
        # Turn the initial list into a heap in-place: O(N)
        heapq.heapify(self.heap)
        
        # Trim down the heap until only the k largest elements remain
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        # Add the new score to the stream
        heapq.heappush(self.heap, val)
        
        # If we have more than k elements, discard the absolute smallest
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
            
        # The root of our min-heap of size k is the kth largest element
        return self.heap[0]