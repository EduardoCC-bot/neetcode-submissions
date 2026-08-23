class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}

        def helper(i, acc):
            if (i, acc) in dp:
                return dp[(i, acc)]

            if i == len(nums):
                return 1 if acc == target  else 0

            dp[i, acc] = (helper(i+1, acc + nums[i]) + 
                helper(i+1, acc - nums[i]))
            
            return dp[(i,acc)]
        
        return helper(0,0)