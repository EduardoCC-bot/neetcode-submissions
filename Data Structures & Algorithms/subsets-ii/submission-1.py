class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets, currSet = [], []

        def helper(i, nums, subsets, currSet):
            if i >= len(nums):
                subsets.append(currSet.copy())
                return
            #Decision add element
            currSet.append(nums[i])
            helper(i+1, nums, subsets, currSet)
            currSet.pop()

            #Desision not add element
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1, nums, subsets, currSet)

        
        helper(0, nums,subsets, currSet)
        return subsets