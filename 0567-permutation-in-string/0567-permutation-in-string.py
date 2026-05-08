class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)
        if n1 > n2:
            return False
        
        # Frequency arrays for lowercase English letters (a-z)
        s1_counts = [0] * 26
        s2_counts = [0] * 26
        
        # Initialize the frequency for s1 and the first window of s2
        for i in range(n1):
            s1_counts[ord(s1[i]) - ord('a')] += 1
            s2_counts[ord(s2[i]) - ord('a')] += 1
        
        # Check how many characters match in the initial window
        matches = 0
        for i in range(26):
            if s1_counts[i] == s2_counts[i]:
                matches += 1
        
        # Slide the window across s2
        for i in range(n2 - n1):
            if matches == 26:
                return True
            
            # Character entering the window from the right
            right_idx = ord(s2[i + n1]) - ord('a')
            s2_counts[right_idx] += 1
            if s2_counts[right_idx] == s1_counts[right_idx]:
                matches += 1
            elif s2_counts[right_idx] == s1_counts[right_idx] + 1:
                matches -= 1
                
            # Character leaving the window from the left
            left_idx = ord(s2[i]) - ord('a')
            s2_counts[left_idx] -= 1
            if s2_counts[left_idx] == s1_counts[left_idx]:
                matches += 1
            elif s2_counts[left_idx] == s1_counts[left_idx] - 1:
                matches -= 1
                
        return matches == 26