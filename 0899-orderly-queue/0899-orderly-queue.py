class Solution:
    def orderlyQueue(self, s: str, k: int) -> str:
        if k == 1:
            # Generate all rotations and find the minimum
            n = len(s)
            res = s
            for i in range(1, n):
                # Form rotation by slicing
                rotation = s[i:] + s[:i]
                if rotation < res:
                    res = rotation
            return res
        else:
            # If k > 1, we can sort the string completely
            return "".join(sorted(s))