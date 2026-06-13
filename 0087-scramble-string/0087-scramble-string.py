from functools import lru_cache
from collections import Counter

class Solution:
    @lru_cache(None)
    def isScramble(self, s1: str, s2: str) -> bool:
        if s1 == s2:
            return True
        
        # Pruning: If character counts don't match, they can't be scrambles
        if Counter(s1) != Counter(s2):
            return False
        
        n = len(s1)
        # Try every possible split point
        for i in range(1, n):
            # Case 1: No swap
            # s1_left matches s2_left AND s1_right matches s2_right
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
                return True
            
            # Case 2: Swap occurred
            # s1_left matches s2_right AND s1_right matches s2_left
            if self.isScramble(s1[:i], s2[n-i:]) and self.isScramble(s1[i:], s2[:n-i]):
                return True
                
        return False