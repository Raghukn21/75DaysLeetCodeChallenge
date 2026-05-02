class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left = 0
        right = len(s) - 1
        
        while left < right:
            # Swap the characters
            s[left], s[right] = s[right], s[left]
            
            # Move the pointers toward each other
            left += 1
            right -= 1