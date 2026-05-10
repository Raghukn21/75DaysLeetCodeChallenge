class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = [] # Stores indices
        max_area = 0
        # Add a 0 at the end to force-pop all remaining elements in the stack
        heights.append(0)
        
        for i, h in enumerate(heights):
            # While the current height is smaller than the height at stack's top
            while stack and h < heights[stack[-1]]:
                # Height of the rectangle is the bar we are popping
                height = heights[stack.pop()]
                
                # Width is determined by the distance between 
                # the current index (right boundary) and the index 
                # now at the top of the stack (left boundary)
                width = i if not stack else i - stack[-1] - 1
                
                max_area = max(max_area, height * width)
            
            stack.append(i)
            
        # Restore heights if you need to reuse the input array (optional)
        heights.pop()
        return max_area