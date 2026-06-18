class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        # Start with the base case
        res = "1"
        
        # Build the sequence up to n
        for _ in range(n - 1):
            next_res = []
            i = 0
            while i < len(res):
                count = 1
                # Count consecutive identical characters
                while i + 1 < len(res) and res[i] == res[i + 1]:
                    i += 1
                    count += 1
                
                # Append count + character
                next_res.append(str(count))
                next_res.append(res[i])
                i += 1
            
            res = "".join(next_res)
            
        return res