class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        f, s = 0, 0
        while True:
            s = nums[s]
            f = nums[nums[f]]
            if s == f:
                break
        
        s2 = 0
        while True:
            s =  nums[s]
            s2 = nums[s2]
            if s == s2:
                return s
        
        
'''
        for i in range(len(nums)):
            if (nums[abs(nums[i]) - 1 ]) < 0:
                return abs(nums[i])
            nums[abs(nums[i]) - 1] *= -1
        return -1

'''