class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        """
        nums = [1,2,3,4]
        """
        if sum(nums) % 2:
            return False

        target = sum(nums) // 2
        dp = [False] * (target + 1)
        dp[0] = True
        for n in nums:
            for j in range(target, n - 1, -1):
                dp[j] = dp[j] or dp[j - n]
        return dp[target]
        