class Solution:
    def countDigitOne(self, n: int) -> int:
        count = 0
        factor = 1
        
        while factor <= n:
            # Split the number into high, current, and low parts
            # Example: n=13, factor=10 (tens place)
            # high = 1, current = 3, low = 0
            high = n // (factor * 10)
            current = (n // factor) % 10
            low = n % factor
            
            if current == 0:
                # If current digit is 0, 1s appear due to higher digits only
                count += high * factor
            elif current == 1:
                # If current digit is 1, 1s appear due to higher digits 
                # plus the remaining portion of the current number
                count += high * factor + (low + 1)
            else:
                # If current digit > 1, 1s appear (high + 1) times
                count += (high + 1) * factor
            
            factor *= 10
            
        return count