class Solution:
    def largestMagicSquare(self, grid):
        m, n = len(grid), len(grid[0])
        
        row = [[0]*(n+1) for _ in range(m)]
        col = [[0]*(n) for _ in range(m+1)]
        
        for i in range(m):
            for j in range(n):
                row[i][j+1] = row[i][j] + grid[i][j]
                col[i+1][j] = col[i][j] + grid[i][j]
        
        def is_magic(x, y, k):
            s = row[x][y+k] - row[x][y]
            
            for i in range(x, x+k):
                if row[i][y+k] - row[i][y] != s:
                    return False
            
            for j in range(y, y+k):
                if col[x+k][j] - col[x][j] != s:
                    return False
            
            d1 = d2 = 0
            for i in range(k):
                d1 += grid[x+i][y+i]
                d2 += grid[x+i][y+k-1-i]
            
            return d1 == s and d2 == s
        
        for k in range(min(m, n), 1, -1):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    if is_magic(i, j, k):
                        return k
        
        return 1
