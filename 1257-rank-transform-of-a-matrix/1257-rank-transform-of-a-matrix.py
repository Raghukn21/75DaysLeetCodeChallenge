class Solution:
    def matrixRankTransform(self, matrix: list[list[int]]) -> list[list[int]]:
        m, n = len(matrix), len(matrix[0])
        res = [[0] * n for _ in range(m)]
        row_max = [0] * m
        col_max = [0] * n
        
        # Store positions for each value
        val_map = {}
        for r in range(m):
            for c in range(n):
                val = matrix[r][c]
                if val not in val_map: val_map[val] = []
                val_map[val].append((r, c))
        
        # Process values in increasing order
        for val in sorted(val_map.keys()):
            cells = val_map[val]
            parent = list(range(len(cells)))
            
            def find(i):
                if parent[i] != i: parent[i] = find(parent[i])
                return parent[i]
            
            def union(i, j):
                root_i, root_j = find(i), find(j)
                if root_i != root_j: parent[root_i] = root_j
            
            # Union cells in the same row/col
            r_map, c_map = {}, {}
            for i, (r, c) in enumerate(cells):
                if r in r_map: union(i, r_map[r])
                if c in c_map: union(i, c_map[c])
                r_map[r] = c_map[c] = i
            
            # Group components
            groups = {}
            for i in range(len(cells)):
                root = find(i)
                if root not in groups: groups[root] = []
                groups[root].append(cells[i])
            
            # Compute ranks for the components
            for group in groups.values():
                rank = 1
                for r, c in group:
                    rank = max(rank, row_max[r] + 1, col_max[c] + 1)
                for r, c in group:
                    res[r][c] = rank
                    row_max[r] = col_max[c] = rank
                    
        return res