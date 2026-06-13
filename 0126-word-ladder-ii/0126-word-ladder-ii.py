from collections import deque, defaultdict

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: list[str]) -> list[list[str]]:
        word_set = set(wordList)
        if endWord not in word_set:
            return []
        
        # BFS to find the shortest distance from beginWord to all reachable words
        distances = {beginWord: 0}
        queue = deque([beginWord])
        graph = defaultdict(set)
        
        while queue:
            curr = queue.popleft()
            for i in range(len(curr)):
                for char in 'abcdefghijklmnopqrstuvwxyz':
                    next_word = curr[:i] + char + curr[i+1:]
                    if next_word in word_set:
                        if next_word not in distances:
                            distances[next_word] = distances[curr] + 1
                            queue.append(next_word)
                        # Build graph of words that are exactly one step closer to start
                        if distances.get(next_word) == distances[curr] + 1:
                            graph[next_word].add(curr)
        
        # DFS to reconstruct all paths from endWord to beginWord
        results = []
        def dfs(curr, path):
            if curr == beginWord:
                results.append(path[::-1])
                return
            for prev in graph[curr]:
                dfs(prev, path + [prev])
        
        dfs(endWord, [endWord])
        return results