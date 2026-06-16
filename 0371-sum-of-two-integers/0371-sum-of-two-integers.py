class Solution:
    def getSum(self, a: int, b: int) -> int:
        # Mask to handle 32-bit integers in languages like C++/Java.
        # Python handles arbitrary precision integers, so we use a mask
        # to simulate 32-bit overflow behavior.
        mask = 0xFFFFFFFF
        
        while b != 0:
            # Calculate the sum without carry and the carry itself
            sum_without_carry = (a ^ b) & mask
            carry = ((a & b) << 1) & mask
            
            a = sum_without_carry
            b = carry
            
        # If the result is negative in 32-bit representation
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)