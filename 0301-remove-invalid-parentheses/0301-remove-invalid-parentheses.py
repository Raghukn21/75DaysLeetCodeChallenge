class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            count = 0
            for char in string:
                if char == '(':
                    count += 1
                elif char == ')':
                    count -= 1
                    if count < 0:
                        return False
            return count == 0

        # BFS initialization
        level = {s}
        while level:
            # Filter all valid strings in the current level
            valid = list(filter(is_valid, level))
            if valid:
                return valid
            
            # Generate next level by removing one parenthesis from each string
            next_level = set()
            for string in level:
                for i in range(len(string)):
                    if string[i] in ('(', ')'):
                        # Create new string by skipping the character at index i
                        next_level.add(string[:i] + string[i+1:])
            level = next_level
            
        return [""]