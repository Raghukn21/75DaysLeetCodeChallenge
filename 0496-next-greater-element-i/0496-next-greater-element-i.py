class Solution:
    def nextGreaterElement(self, nums1: list[int], nums2: list[int]) -> list[int]:
        # Map to store the next greater element for each number in nums2
        next_greater_map = {}
        stack = []

        # Process nums2 to find next greater elements using a monotonic stack
        for num in nums2:
            while stack and num > stack[-1]:
                smaller_num = stack.pop()
                next_greater_map[smaller_num] = num
            stack.append(num)

        # Build the result for nums1 by looking up values in our map
        return [next_greater_map.get(n, -1) for n in nums1]