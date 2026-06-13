class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_ptr, p_ptr = 0, 0
        star_idx = -1
        s_tmp_idx = -1
        
        while s_ptr < len(s):
            # Case 1: Direct match or '?'
            if p_ptr < len(p) and (p[p_ptr] == '?' or p[p_ptr] == s[s_ptr]):
                s_ptr += 1
                p_ptr += 1
            # Case 2: '*' found, record positions
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star_idx = p_ptr
                s_tmp_idx = s_ptr
                p_ptr += 1
            # Case 3: Mismatch, but we have a previous '*'
            elif star_idx != -1:
                p_ptr = star_idx + 1
                s_tmp_idx += 1
                s_ptr = s_tmp_idx
            # Case 4: Mismatch, no '*'
            else:
                return False
        
        # Check if remaining characters in p are all '*'
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1
            
        return p_ptr == len(p)