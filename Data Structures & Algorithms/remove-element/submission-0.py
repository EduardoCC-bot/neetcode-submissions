class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l , r = 0, len(nums) - 1 # 0, 7

        while l <= r: # 0 <= 7 | 1 <= 7
            if nums[l] == val: # [0] == 2  
                tmp = nums[r] 
                nums[r] = nums[l]
                nums[l] = tmp
                r-=1
            else:  
                l+=1 # l = 1
        
        return l