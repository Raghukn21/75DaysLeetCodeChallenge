class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        
        # Reverse the string
        rev_s = s[::-1]
        
        # Build the combined string
        temp = s + "#" + rev_s
        
        # Compute KMP table (Failure Function)
        n = len(temp)
        lps = [0] * n
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and temp[i] != temp[j]:
                j = lps[j - 1]
            if temp[i] == temp[j]:
                j += 1
            lps[i] = j
            
        # The last value in lps is the length of the longest palindromic prefix
        longest_palindrome_prefix_len = lps[-1]
        
        # Take the suffix that is NOT part of the palindrome, reverse it, 
        # and add it to the front
        suffix_to_add = s[longest_palindrome_prefix_len:][::-1]
        return suffix_to_add + s