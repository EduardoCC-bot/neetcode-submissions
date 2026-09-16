class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = [False for i in range(len(nums))]
        res = []
        def helper(curr, n):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for j in range(len(n)):
                if not n[j]:
                    curr.append(nums[j])
                    n[j] = True
                    helper(curr, n)
                    curr.pop()
                    n[j] = False
                

        helper([], n)
        return res




        