class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        """
        Case interval full outside
        [[1,2],[3,5],[9,10]]
        
        [6,7]
        [[1,2],[3,5],[6,7],[9,10]]
        
        Case full inside
        [[1,3],[4,6]]
        [2,5]
        [[1,6]]

        case mid inside

        """
        if not intervals:
            return [newInterval]
        
        n = len(intervals)
        start = newInterval[0] 

        l, r  = 0, n - 1

        while l <= r:
            m = (l + r)// 2
            if intervals[m][0] < start:
                l = m + 1
            else:
                r = m - 1
        
        intervals.insert(l, newInterval)
        
        res = []
        for interval in intervals:
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res

        

             




