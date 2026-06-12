from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: list[str]) -> list[int]:
        if not s or not words:
            return []
            
        word_len = len(words[0])
        num_words = len(words)
        total_len = word_len * num_words
        word_counts = Counter(words)
        res = []
        
        # We only need to check offsets from 0 to word_len - 1
        for i in range(word_len):
            left = i
            window_counts = Counter()
            words_in_window = 0
            
            for right in range(i, len(s) - word_len + 1, word_len):
                word = s[right : right + word_len]
                
                if word in word_counts:
                    window_counts[word] += 1
                    words_in_window += 1
                    
                    # If word count exceeds original, shrink window from left
                    while window_counts[word] > word_counts[word]:
                        left_word = s[left : left + word_len]
                        window_counts[left_word] -= 1
                        words_in_window -= 1
                        left += word_len
                    
                    # If window matches, record result
                    if words_in_window == num_words:
                        res.append(left)
                else:
                    # Reset window
                    window_counts.clear()
                    words_in_window = 0
                    left = right + word_len
                    
        return res