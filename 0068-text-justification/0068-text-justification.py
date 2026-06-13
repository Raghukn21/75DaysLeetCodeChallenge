class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        res, cur, num_of_letters = [], [], 0
        
        for w in words:
            # If adding the word exceeds the width, justify the current line
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                res.append("".join(cur))
                cur, num_of_letters = [], 0
            
            cur.append(w)
            num_of_letters += len(w)
            
        # Handle the last line (left-justified)
        res.append(" ".join(cur).ljust(maxWidth))
        return res