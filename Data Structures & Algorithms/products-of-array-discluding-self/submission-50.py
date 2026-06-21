class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        sufix = []
        res = []
        acum = 1

        for i in range(len(nums)):
            acum = acum * nums[i]
            prefix.append(acum)
        
        acum = 1
        for i in range(len(nums) - 1, -1, -1):
            acum = acum*nums[i]
            sufix.append(acum)
        sufix.reverse()

        for i in range(len(nums)):
            if i == 0:
                res.append(sufix[i+1])
            elif  i == (len(nums)-1):
                res.append(prefix[i-1])
            else:
                res.append(prefix[i-1]*sufix[i+1])
        return res
