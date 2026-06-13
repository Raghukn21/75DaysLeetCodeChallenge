class Solution:
    def longestValidParentheses(self, s: str) -> int:
        max_len = 0
        stack = [-1]  # Base index for valid sequence calculation
        
        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    # Current char is a mismatch, use it as the new base
                    stack.append(i)
                else:
                    # Found a valid sequence, update max_len
                    max_len = max(max_len, i - stack[-1])
                    
        return max_len