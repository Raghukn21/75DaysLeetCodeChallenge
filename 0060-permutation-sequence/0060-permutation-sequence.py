import math

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create a list of available numbers: [1, 2, ..., n]
        numbers = [str(i) for i in range(1, n + 1)]
        k -= 1  # Adjust k to 0-indexed for easier math
        
        factorial = math.factorial(n - 1)
        permutation = []
        
        for i in range(n - 1, 0, -1):
            index = k // factorial
            permutation.append(numbers.pop(index))
            
            # Update k and factorial for the next position
            k %= factorial
            factorial //= i
            
        # Append the last remaining number
        permutation.append(numbers[0])
        
        return "".join(permutation)