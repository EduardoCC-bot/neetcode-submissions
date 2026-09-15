class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = [False for i in range(len(nums))]
        s = len(nums)
        res = []
        def helper(i, curr, n):
            if len(curr) == s:
                res.append(curr.copy())
                return

            for j in range(len(n)):
                if not n[j]:
                    curr.append(nums[j])
                    n[j] = True
                    helper(j, curr, n)
                    curr.pop()
                    n[j] = False
        helper(0, [], n)
        return res