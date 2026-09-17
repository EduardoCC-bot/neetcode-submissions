class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        target = 0
        [-1,0,1,2,-1,-4]
        [-4,-1,-1,0,1,2]
        """
        nums.sort()
        i = 0
        res = []
        pivot = float('inf')
        for i in range(len(nums)):
            if nums[i] == pivot:
                continue
            pivot = nums[i]
            l, r = i + 1, len(nums) - 1
            while l < r:
                curSum = pivot + nums[l] + nums[r]
                if curSum == 0:
                    res.append([pivot, nums[l], nums[r]])
                    cur = nums[l]
                    while l < len(nums) and nums[l] == cur:
                        l += 1
                    cur = nums[r]
                    while r > 0 and nums[r] == cur:
                        r -= 1
                elif curSum < 0:
                    l += 1
                elif curSum > 0:
                    r -= 1
        return res
            
            

            




