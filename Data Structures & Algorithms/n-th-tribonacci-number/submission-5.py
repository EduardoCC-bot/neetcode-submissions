class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = [0] * (n + 1)
        if n <= 2: return 1 if n != 0 else 0
        #Base case
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        # n = 3
        #[0,1,1,2,0]
        for i in range(3, n + 1):
            dp[i] = dp[i-3] + dp[i-2] + dp[i-1] # i = 3 -> 1 + 1 = 2
        return dp[n]

        