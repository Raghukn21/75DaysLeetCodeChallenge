class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int:
        # Array to track the net trust score for each person (1-indexed)
        trust_scores = [0] * (n + 1)
        
        # Calculate net trust scores
        for a, b in trust:
            trust_scores[a] -= 1  # Person 'a' trusts someone, decrease score
            trust_scores[b] += 1  # Person 'b' is trusted, increase score
            
        # The judge must have a net score of exactly n - 1
        for i in range(1, n + 1):
            if trust_scores[i] == n - 1:
                return i
                
        return -1