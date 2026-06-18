class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for n in numSet:
            if(n-1) not in numSet:
                cnt = 0
                while n+cnt in numSet:
                    cnt+=1
                res = max(res, cnt)
        return res


