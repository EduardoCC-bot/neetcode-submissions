class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = []
        remider = {0: -1}
        
        total = 0
        for i, n in enumerate(nums):
            total +=  n
            r = total % k
            if r not in remider:
                remider[r] = i 
            elif i - remider[r] > 1:
                return True
        return False