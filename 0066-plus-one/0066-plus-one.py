class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        n = len(digits)
        
        # Traverse the digits from right to left
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            # If the digit is 9, it becomes 0 and the carry propagates
            digits[i] = 0
            
        # If we are here, it means all digits were 9s
        # Prepend a 1 to the beginning
        return [1] + digits