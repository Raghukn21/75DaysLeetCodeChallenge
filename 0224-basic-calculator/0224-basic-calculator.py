class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        result = 0
        number = 0
        sign = 1  # 1 for '+', -1 for '-'
        
        for char in s:
            if char.isdigit():
                number = number * 10 + int(char)
            elif char == '+':
                result += sign * number
                number = 0
                sign = 1
            elif char == '-':
                result += sign * number
                number = 0
                sign = -1
            elif char == '(':
                # Push the result and sign onto the stack to save the state
                stack.append(result)
                stack.append(sign)
                # Reset variables for the new sub-expression
                result = 0
                sign = 1
            elif char == ')':
                # Complete the sub-expression
                result += sign * number
                number = 0
                # Apply the sign saved before the '('
                result *= stack.pop()
                # Add the result to the previous scope's result
                result += stack.pop()
                
        # Final addition for any remaining number
        result += sign * number
        return result