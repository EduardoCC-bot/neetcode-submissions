class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        m = 3, n = 3
      ->[0][0][0]
        [0][0][0]
        [0][0][0]<-

        r, c = m - 1, n - 1         
        """

        dp = [[-1] * n for _ in range(m)] 
        def dfs(i, j):
            if i >= m or j >= n:
                return 0

            if i == (m - 1) and j == (n - 1):
                return 1
            
            if dp[i][j] != -1:
                return dp[i][j]
            dp[i][j] = dfs(i, j + 1) + dfs(i + 1, j)
            return dp[i][j]
        return dfs(0, 0)

