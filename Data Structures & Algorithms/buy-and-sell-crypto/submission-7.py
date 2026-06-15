class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = 0 
        for i in range(len(prices)):
            b = prices[i]
            for j in range(i + 1, len(prices)):
                s = prices[j]
                res = max(res, s-b)
        return res