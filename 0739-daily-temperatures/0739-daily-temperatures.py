class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        n = len(temperatures)
        answer = [0] * n
        stack = []  # To store indices

        for i, curr_temp in enumerate(temperatures):
            # Monotonic stack logic
            while stack and curr_temp > temperatures[stack[-1]]:
                prev_index = stack.pop()
                answer[prev_index] = i - prev_index
            
            stack.append(i)
            
        return answer