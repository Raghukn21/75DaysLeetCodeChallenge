class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        i, j = len(a) - 1, len(b) - 1
        carry = 0
        
        while i >= 0 or j >= 0 or carry:
            # Get digits from a and b, or 0 if we've reached the start
            val_a = int(a[i]) if i >= 0 else 0
            val_b = int(b[j]) if j >= 0 else 0
            
            # Calculate sum and new carry
            total = val_a + val_b + carry
            result.append(str(total % 2))
            carry = total // 2
            
            i -= 1
            j -= 1
            
        # Reverse the result since we appended digits from right to left
        return "".join(result[::-1])