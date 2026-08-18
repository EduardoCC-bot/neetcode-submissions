class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        sort array [[1,3],[1,5],[6,7]]
        list start 1,1,6    1,2 
        list end   3,5,7    2,3
        
        """
        intervals.sort(key=lambda pair: pair[0])
        output = [intervals[0]]

        for st, nd in intervals:
            lastend = output[-1][1]

            if st <= lastend:
                output[-1][1] = max(lastend, nd)
            else:
                output.append([st, nd]) 

        return output
        

