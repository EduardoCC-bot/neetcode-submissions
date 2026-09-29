class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
        [[1,2],[2,4],[1,4]]
        [[1,2], [1,4], [2,4]]
        start = 1
        end = 2

        istart = 1
        iend = 4

        istart = 2
        iend = 4
        [[1,2], [2,4]]

        """
        intervals.sort()
        res = 0
        prevEnd = intervals[0][1]
        for start, end in intervals[1:]:
            if start >= prevEnd: 
                prevEnd = end
            else:
                res += 1
                prevEnd =min (end, prevEnd)
        return res
