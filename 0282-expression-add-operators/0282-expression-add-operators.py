class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        results = []
        
        def backtrack(index, path, current_val, prev_val):
            # Base case: if we've used all digits
            if index == len(num):
                if current_val == target:
                    results.append(path)
                return
            
            for i in range(index, len(num)):
                # Handle multi-digit numbers (no leading zeros)
                if i > index and num[index] == '0':
                    break
                
                val_str = num[index:i+1]
                val = int(val_str)
                
                if index == 0:
                    # First number, no operator
                    backtrack(i + 1, val_str, val, val)
                else:
                    # Addition
                    backtrack(i + 1, path + "+" + val_str, current_val + val, val)
                    # Subtraction
                    backtrack(i + 1, path + "-" + val_str, current_val - val, -val)
                    # Multiplication
                    # (current_val - prev_val) removes the previous operand, 
                    # then we apply multiplication to prev_val and add it back
                    backtrack(i + 1, path + "*" + val_str, current_val - prev_val + (prev_val * val), prev_val * val)
        
        backtrack(0, "", 0, 0)
        return results