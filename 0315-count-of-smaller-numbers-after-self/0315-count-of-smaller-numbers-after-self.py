class Solution:
    def countSmaller(self, nums: list[int]) -> list[int]:
        n = len(nums)
        count = [0] * n
        # Store (value, original_index) to keep track after sorting
        indexed_nums = list(enumerate(nums))
        
        def merge_sort(arr):
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])
            right = merge_sort(arr[mid:])
            
            return merge(left, right)
            
        def merge(left, right):
            merged = []
            i = j = 0
            while i < len(left) and j < len(right):
                if left[i][1] <= right[j][1]:
                    # left[i] is smaller or equal; update its count 
                    # by how many from 'right' were already moved
                    count[left[i][0]] += j
                    merged.append(left[i])
                    i += 1
                else:
                    merged.append(right[j])
                    j += 1
            
            # Append remaining elements
            while i < len(left):
                count[left[i][0]] += j
                merged.append(left[i])
                i += 1
            merged.extend(right[j:])
            return merged
            
        merge_sort(indexed_nums)
        return count