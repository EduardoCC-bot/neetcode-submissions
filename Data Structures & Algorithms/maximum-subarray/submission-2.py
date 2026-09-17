class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        bestSum = nums[0]
        curSum = 0
        for n in nums:
            curSum = max(curSum + n, n)
            bestSum = max(curSum, bestSum)
        return bestSum