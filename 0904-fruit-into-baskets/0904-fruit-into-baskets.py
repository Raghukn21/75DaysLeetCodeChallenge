from typing import List

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Dictionary to store the count of each fruit type in the current window
        basket = {}
        left = 0
        max_fruits = 0
        
        for right in range(len(fruits)):
            # Add the current fruit to the basket
            current_fruit = fruits[right]
            basket[current_fruit] = basket.get(current_fruit, 0) + 1
            
            # If we have more than 2 types of fruits, shrink the window from the left
            while len(basket) > 2:
                left_fruit = fruits[left]
                basket[left_fruit] -= 1
                
                # If the count drops to zero, remove the fruit type entirely
                if basket[left_fruit] == 0:
                    del basket[left_fruit]
                
                left += 1
            
            # Update the maximum fruits collected so far
            # The window size is (right - left + 1)
            max_fruits = max(max_fruits, right - left + 1)
            
        return max_fruits