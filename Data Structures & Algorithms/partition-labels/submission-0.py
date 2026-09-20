class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        indexs = {}

        for i,c in enumerate(s):
            indexs[c] = i
        
        res = []
        size = end = 0
        for i, c in enumerate(s):
            size +=  1
            end = max(end, indexs[c])

            if i == end:
                res.append(size)
                size = 0
        return res
            