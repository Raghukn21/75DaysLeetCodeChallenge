class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # Stores the complete word at the leaf node

    def remove_word(self, word: str):
        # Helper function to prune the Trie from bottom up once a word is found
        def dfs(node, index):
            if index == len(word):
                node.word = None
                return len(node.children) == 0
            
            char = word[index]
            if char in node.children:
                should_delete = dfs(node.children[char], index + 1)
                if should_delete:
                    del node.children[char]
                    return len(node.children) == 0 and node.word is None
            return False
        
        dfs(self, 0)


class Solution:
    def findWords(self, board: list[list[str]], words: list[str]) -> list[str]:
        # 1. Build the Trie
        root = TrieNode()
        for w in words:
            curr = root
            for char in w:
                if char not in curr.children:
                    curr.children[char] = TrieNode()
                curr = curr.children[char]
            curr.word = w
            
        ROWS, COLS = len(board), len(board[0])
        result = []
        
        # 2. Define the Backtracking DFS function
        def dfs(r, c, node):
            char = board[r][c]
            
            # If the current character sequence isn't in the Trie, stop
            if char not in node.children:
                return
                
            next_node = node.children[char]
            
            # If we match a full word, add it to results and prune it
            if next_node.word:
                result.append(next_node.word)
                root.remove_word(next_node.word) # Prune to prevent finding duplicates
                
            # Mark the current cell as visited
            board[r][c] = "#"
            
            # Explore 4 neighboring directions: Up, Down, Left, Right
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = r + dr, c + dc
                if 0 <= nr < ROWS and 0 <= nc < COLS and board[nr][nc] != "#":
                    dfs(nr, nc, next_node)
                    
            # Restore the cell (Backtrack)
            board[r][c] = char

        # 3. Traverse every starting cell on the board
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root)
                
        return result