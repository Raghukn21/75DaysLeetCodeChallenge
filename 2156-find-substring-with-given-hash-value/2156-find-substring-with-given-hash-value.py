class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        current_hash = 0
        pk = pow(power, k - 1, modulo)
        
        # Calculate initial hash for the last window (starting at index n-k)
        # We process from right to left to simplify rolling logic
        for i in range(n - 1, n - 1 - k, -1):
            val = ord(s[i]) - ord('a') + 1
            current_hash = (current_hash * power + val) % modulo
            
        ans_idx = n - k
        
        # Slide window from right to left
        for i in range(n - 1 - k, -1, -1):
            # Remove s[i+k] and add s[i]
            # H = ((H - val(s[i+k])*p^(k-1)) * power + val(s[i])) % modulo
            val_out = ord(s[i + k]) - ord('a') + 1
            val_in = ord(s[i]) - ord('a') + 1
            
            current_hash = (current_hash - val_out * pk) % modulo
            current_hash = (current_hash * power + val_in) % modulo
            
            if current_hash == hashValue:
                ans_idx = i
                
        return s[ans_idx : ans_idx + k]