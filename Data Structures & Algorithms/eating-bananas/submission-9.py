class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        [1,4,3,2] h = 9

        maximun is max of list
        1    4
        4 hours
        4 // 2 = 2
        7 hours k = 2
        """
        l, r = 1, max(piles)
        if len(piles) > h: return False
        res = r
        while l <= r:
            k = (l + r) // 2
            hours = 0
            for p in piles:
                hours += math.ceil(float(p) / k)
            if hours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res

