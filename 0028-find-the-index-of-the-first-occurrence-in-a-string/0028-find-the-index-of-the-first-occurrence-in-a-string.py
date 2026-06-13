class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_len = len(haystack)
        n_len = len(needle)
        
        # Optimization: loop only up to the point where needle can fit
        for i in range(h_len - n_len + 1):
            if haystack[i : i + n_len] == needle:
                return i
                
        return -1