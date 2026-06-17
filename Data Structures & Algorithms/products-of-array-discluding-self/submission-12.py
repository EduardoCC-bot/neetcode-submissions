class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        acum = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if(i != j):
                    acum = acum * nums[j]
            
            res.append(acum)
            acum = 1
        return res