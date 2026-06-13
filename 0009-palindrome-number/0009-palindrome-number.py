class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Convert integer to string and use the two-pointer approach
        s = str(x)
        left, right = 0, len(s) - 1
        
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True