class Solution:
    def countRangeSum(self, nums: list[int], lower: int, upper: int) -> int:
        # Generate prefix sums: P[i] = sum(nums[0...i-1])
        prefix_sums = [0]
        for x in nums:
            prefix_sums.append(prefix_sums[-1] + x)
            
        def count_while_merge_sort(left, right):
            if right - left <= 1:
                return 0
            
            mid = (left + right) // 2
            count = count_while_merge_sort(left, mid) + count_while_merge_sort(mid, right)
            
            # Count valid ranges
            j = k = mid
            for i in range(left, mid):
                while k < right and prefix_sums[k] - prefix_sums[i] < lower:
                    k += 1
                while j < right and prefix_sums[j] - prefix_sums[i] <= upper:
                    j += 1
                count += (j - k)
            
            # Standard merge step to maintain sorted order
            prefix_sums[left:right] = sorted(prefix_sums[left:right])
            return count
            
        return count_while_merge_sort(0, len(prefix_sums))