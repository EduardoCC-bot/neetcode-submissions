class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Input: nums = [1,12,-5,-6,50,3], k = 4
            [1, 13, 8, 2, 51, 42]
            []

            [0.5, 12.75, 10.5]

        """
        res = float('-inf')
        for s in range(len(nums) - k + 1):
            sum_val = 0
            for i in range(s, len(nums)):
                sum_val += nums[i]

                if i - s + 1 >= k:
                    res = max(res, sum_val / (i - s + 1))
            
        return res