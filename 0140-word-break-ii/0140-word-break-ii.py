class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        word_set = set(wordDict)
        memo = {}

        def dfs(string):
            # Return cached result if available
            if string in memo:
                return memo[string]
            
            # Base case: if string is empty, return list with empty string to build on
            if not string:
                return [""]
            
            res = []
            # Explore all possible prefix cuts
            for i in range(1, len(string) + 1):
                prefix = string[:i]
                if prefix in word_set:
                    # Get all valid sentences for the remaining suffix
                    suffixes = dfs(string[i:])
                    for suffix in suffixes:
                        res.append((prefix + " " + suffix).strip())
            
            memo[string] = res
            return res

        return dfs(s)