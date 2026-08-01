class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # nums=[1,3,5,7,9]
        # 6
        """
            l = 0
            r = 4
            m = 0 + 4 - 0 // 2 = 2
            nums[m] = 5
            5 < target
            l = 2+ 1 = 31
            index = 3
            l = 3 r = 4
            m = 3 + (4 - 3) // 2: 3
            nums[m] = 7
            7 > 6
            r = m - 1 = 2
            index = m = 2 nums[index] = 5
        """
        res = len(nums)
        l, r = 0, len(nums) - 1
        while l <= r:
            m  = l + (r - l) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                res = m
                r = m - 1
            else:
                return m
        return res



