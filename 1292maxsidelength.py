class Solution:
    def maxSideLength(self, mat, threshold):
        m, n = len(mat), len(mat[0])
        
        ps = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                ps[i+1][j+1] = mat[i][j] + ps[i][j+1] + ps[i+1][j] - ps[i][j]
        
        def possible(k):
            for i in range(m - k + 1):
                for j in range(n - k + 1):
                    s = ps[i+k][j+k] - ps[i][j+k] - ps[i+k][j] + ps[i][j]
                    if s <= threshold:
                        return True
            return False
        
        l, r, an = 1, min(m, n), 0
        while l <= r:
            mid = (l + r) // 2
            if possible(mid):
                ans = mid
                l = mid + 1
            else:
                r = mid - 1
        
        return an
