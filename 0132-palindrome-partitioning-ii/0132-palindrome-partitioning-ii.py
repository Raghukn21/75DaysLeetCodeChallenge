class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # is_pal[i][j] will be True if s[i...j] is a palindrome
        is_pal = [[False] * n for _ in range(n)]
        # cuts[i] is the min cuts for s[0...i-1]
        cuts = [i - 1 for i in range(n + 1)]
        
        for j in range(n):
            for i in range(j + 1):
                # Check if s[i...j] is a palindrome
                if s[i] == s[j] and (j - i < 2 or is_pal[i + 1][j - 1]):
                    is_pal[i][j] = True
                    # If s[0...j] is a palindrome, 0 cuts needed
                    if i == 0:
                        cuts[j + 1] = 0
                    else:
                        # Otherwise, take min of previous cuts + 1
                        cuts[j + 1] = min(cuts[j + 1], cuts[i] + 1)
                        
        return cuts[n]