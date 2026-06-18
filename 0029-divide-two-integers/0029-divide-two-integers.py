class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit signed integer range
        MAX_INT = 2**31 - 1
        MIN_INT = -2**31
        
        # Handle overflow case for -2^31 / -1
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT
        
        # Determine the sign
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values
        a, b = abs(dividend), abs(divisor)
        quotient = 0
        
        # Perform bitwise division
        while a >= b:
            temp_b, count = b, 1
            # Double temp_b (equivalent to multiplying by 2) until it's larger than a
            while a >= (temp_b << 1):
                temp_b <<= 1
                count <<= 1
            
            # Subtract the largest found multiple and add to quotient
            a -= temp_b
            quotient += count
            
        return -quotient if negative else quotient