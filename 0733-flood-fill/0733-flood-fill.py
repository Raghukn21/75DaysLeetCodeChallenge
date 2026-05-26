class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        rows, cols = len(image), len(image[0])
        start_color = image[sr][sc]
        
        # If the starting pixel already has the target color, no changes are needed.
        if start_color == color:
            return image
        
        def dfs(r: int, c: int):
            # Base case: if out of bounds or not matching the starting color, stop.
            if r < 0 or r >= rows or c < 0 or c >= cols or image[r][c] != start_color:
                return
            
            # Update the color of the current pixel
            image[r][c] = color
            
            # Recursively walk to 4-directional neighbors
            dfs(r + 1, c) # Down
            dfs(r - 1, c) # Up
            dfs(r, c + 1) # Right
            dfs(r, c - 1) # Left

        # Start the flood fill from the given coordinates
        dfs(sr, sc)
        return image