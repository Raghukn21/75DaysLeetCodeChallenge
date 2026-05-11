class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curr_str = ""
        curr_num = 0
        
        for char in s:
            if char.isdigit():
                # Build the number (handles cases like '300')
                curr_num = curr_num * 10 + int(char)
            elif char == '[':
                # Push the current string and the multiplier onto the stack
                stack.append((curr_str, curr_num))
                # Reset for the content inside the brackets
                curr_str = ""
                curr_num = 0
            elif char == ']':
                # Pop the context from before the matching '['
                prev_str, num = stack.pop()
                # Repeat the current string and prepend the previous context
                curr_str = prev_str + (num * curr_str)
            else:
                # It's a plain letter, just add to current working string
                curr_str += char
                
        return curr_str