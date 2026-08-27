class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        i = 0

        while i < len(nums):
            cnt = 0
            while i < len(nums) and nums[i] == 1:
                cnt+=1
                i+=1
            res = max(cnt, res)
            i += 1

        return res