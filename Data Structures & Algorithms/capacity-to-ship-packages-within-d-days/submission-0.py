class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def getNumDays(mid) -> bool:
            ships, currmid = 1, mid
            for w in weights:
                if currmid - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    currmid = mid
                currmid -= w
            return True

        while l <= r:
            mid = (l + r) // 2
            if getNumDays(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
            
        return res

            