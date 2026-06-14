class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            # Shift result to the left to make space for the incoming bit
            result = (result << 1) | (n & 1)
            # Shift n to the right to process the next bit
            n >>= 1
        return result