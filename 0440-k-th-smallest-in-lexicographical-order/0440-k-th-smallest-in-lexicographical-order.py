class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        def count_steps(curr, n):
            steps = 0
            first, last = curr, curr
            while first <= n:
                # Add the count of numbers in the current level
                steps += min(n, last) - first + 1
                # Move to the next level
                first *= 10
                last = last * 10 + 9
            return steps

        curr = 1
        k -= 1 # Since we start at the first number
        
        while k > 0:
            steps = count_steps(curr, n)
            if steps <= k:
                # Skip subtree
                k -= steps
                curr += 1
            else:
                # Go deeper
                k -= 1
                curr *= 10
        
        return curr