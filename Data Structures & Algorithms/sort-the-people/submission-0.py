class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        mapa = {}

        for i in range(len(names)):
            mapa[heights[i]] = names[i]
        
        heights.sort()
        res = []
        for i in range(len(heights)-1,-1,-1):
            res.append(mapa[heights[i]])
        
        return res