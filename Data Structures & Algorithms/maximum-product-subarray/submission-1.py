class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = float('-inf')
        prod = 1
        prev = 1
        for n in nums:
            tmp = prod * n
            prod = max(n * prod, n * prev, n)
            prev = min(tmp, n * prev, n)
            res = max(res, prod)
        return res

