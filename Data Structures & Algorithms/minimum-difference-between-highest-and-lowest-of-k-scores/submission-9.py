class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        l, r = 0, k - 1
        nums.sort()
        res = float('inf')
        for r in range( k - 1, len(nums)):
            l = r - (k - 1)
            res = min(res, nums[r] - nums[l])
        return res