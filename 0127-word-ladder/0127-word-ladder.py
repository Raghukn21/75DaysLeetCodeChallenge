from collections import deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: list[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0
        
        queue = deque([(beginWord, 1)])
        
        while queue:
            curr_word, dist = queue.popleft()
            
            if curr_word == endWord:
                return dist
            
            # Try changing each character of the word
            for i in range(len(curr_word)):
                original_char = curr_word[i]
                for char_code in range(ord('a'), ord('z') + 1):
                    new_char = chr(char_code)
                    if new_char == original_char:
                        continue
                    
                    transformed_word = curr_word[:i] + new_char + curr_word[i+1:]
                    
                    if transformed_word in word_set:
                        queue.append((transformed_word, dist + 1))
                        word_set.remove(transformed_word) # Mark as visited
                        
        return 0