class Solution:
    def maxNumber(self, nums1: list[int], nums2: list[int], k: int) -> list[int]:
        def get_max_subsequence(nums, length):
            """Finds the lexicographically largest subsequence of given length."""
            stack = []
            to_drop = len(nums) - length
            for num in nums:
                while to_drop > 0 and stack and stack[-1] < num:
                    stack.pop()
                    to_drop -= 1
                stack.append(num)
            return stack[:length]

        def merge(sub1, sub2):
            """Merges two subsequences to form the lexicographically largest one."""
            res = []
            while sub1 or sub2:
                # Choose the larger list to append from
                if sub1 > sub2:
                    res.append(sub1.pop(0))
                else:
                    res.append(sub2.pop(0))
            return res

        m, n = len(nums1), len(nums2)
        best_sequence = []
        
        # Iterate over how many digits to take from nums1
        for i in range(max(0, k - n), min(k, m) + 1):
            sub1 = get_max_subsequence(nums1, i)
            sub2 = get_max_subsequence(nums2, k - i)
            candidate = merge(sub1, sub2)
            
            if candidate > best_sequence:
                best_sequence = candidate
                
        return best_sequence