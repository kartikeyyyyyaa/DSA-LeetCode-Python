class Solution:
    def maxDotProduct(self, nums1: list[int], nums2: list[int]) -> int:
        n = len(nums1)
        m = len(nums2)
        dp = [[float('-inf')] * m for _ in range(n)]
        
        for i in range(n):
            for j in range(m):
                curr_product = nums1[i] * nums2[j]
                if i > 0 and j > 0:
                    curr_product += max(0, dp[i-1][j-1])
                dp[i][j] = curr_product
                if i > 0:
                    dp[i][j] = max(dp[i][j], dp[i-1][j])
                if j > 0:
                    dp[i][j] = max(dp[i][j], dp[i][j-1])
                    
        return dp[n-1][m-1]