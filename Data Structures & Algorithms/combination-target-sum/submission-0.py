class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def helper(i, acc, curr):
            if acc == target:
                res.append(curr.copy())
                return
            if i >= len(nums) or acc > target:
                return
            
            curr.append(nums[i])
            helper(i, acc + nums[i], curr)
            curr.pop()
            helper(i + 1,acc, curr)

        helper(0, 0, [])    
        return res
