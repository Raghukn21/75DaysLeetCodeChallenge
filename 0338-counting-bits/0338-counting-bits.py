class Solution:
    def countBits(self, n: int) -> list[int]:
        # Initialize the array with 0s of size n + 1
        ans = [0] * (n + 1)
        
        # Build the array using DP
        for i in range(1, n + 1):
            # ans[i >> 1] is the count for i // 2
            # i & 1 is 1 if i is odd, 0 if even
            ans[i] = ans[i >> 1] + (i & 1)
            
        return ans