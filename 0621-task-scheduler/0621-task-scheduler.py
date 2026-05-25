from collections import Counter

class Solution:
    def leastInterval(self, tasks: list[str], n: int) -> int:
        # Step 1: Count the frequencies of each task
        task_counts = Counter(tasks)
        frequencies = list(task_counts.values())
        
        # Step 2: Find the maximum frequency
        max_freq = max(frequencies)
        
        # Step 3: Count how many tasks have this maximum frequency
        max_freq_count = frequencies.count(max_freq)
        
        # Step 4: Calculate the minimum intervals based on the formula
        # (max_freq - 1) groups of size (n + 1), plus the remaining tasks that share the max frequency
        minimum_intervals = (max_freq - 1) * (n + 1) + max_freq_count
        
        # Step 5: Return the larger of the formula result or the actual number of tasks
        return max(len(tasks), minimum_intervals)