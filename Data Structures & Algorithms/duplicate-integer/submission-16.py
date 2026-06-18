class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashSet = set(nums)
        print (len(nums))
        print (len(hashSet))
        return not len(nums) ==  len(hashSet)

            
            
                    
        