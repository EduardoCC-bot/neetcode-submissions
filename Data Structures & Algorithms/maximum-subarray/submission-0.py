class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        best_sum = nums[0]
        currsum = 0
        for n in nums:
            currsum = max(n, currsum + n) 
            best_sum = max(best_sum, currsum)
        
        return best_sum