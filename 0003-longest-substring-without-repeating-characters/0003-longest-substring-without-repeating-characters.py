class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # Stores the last seen index of a character
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            char = s[right]
            
            # If we've seen this char and it's within our current window
            if char in char_map and char_map[char] >= left:
                # Move left to one position past the last occurrence
                left = char_map[char] + 1
            
            # Update the last seen index of the character
            char_map[char] = right
            
            # Calculate window size and update max
            current_window_len = right - left + 1
            if current_window_len > max_length:
                max_length = current_window_len
                
        return max_length
        