import heapq

class Solution:
    def getSkyline(self, buildings: list[list[int]]) -> list[list[int]]:
        # Collect all unique x-coordinates of events
        events = []
        for L, R, H in buildings:
            events.append((L, -H, R))
            events.append((R, 0, 0))
        
        # Sort events by x
        events.sort()
        
        # res stores key points: [x, height]
        # live_buildings stores: (-height, end_x)
        res = [[0, 0]]
        live_buildings = [(0, float('inf'))]
        
        for x, neg_h, R in events:
            # Add building to heap
            if neg_h != 0:
                heapq.heappush(live_buildings, (neg_h, R))
            
            # Remove buildings that are no longer active at x
            while live_buildings[0][1] <= x:
                heapq.heappop(live_buildings)
            
            # Get current max height
            current_max_h = -live_buildings[0][0]
            
            # If height changed, we found a new key point
            if res[-1][1] != current_max_h:
                res.append([x, current_max_h])
                
        return res[1:]