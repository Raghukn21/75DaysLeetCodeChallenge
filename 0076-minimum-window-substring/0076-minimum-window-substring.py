from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Count characters in t
        t_count = Counter(t)
        required = len(t_count)
        
        # Window variables
        left, right = 0, 0
        formed = 0
        window_counts = {}
        
        # (window_size, left, right)
        ans = float("inf"), None, None
        
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            
            # If the current character is in t and matches the required count
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            
            # Try to shrink the window
            while left <= right and formed == required:
                char = s[left]
                
                # Update smallest window
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                
                # Remove character from window
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                
                left += 1
            
            right += 1
            
        return "" if ans[0] == float("inf") else s[ans[1] : ans[2] + 1]