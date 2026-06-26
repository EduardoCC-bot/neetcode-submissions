class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        res = []
        l = 0
        stack = []
        for i in range(len(heights)):
            while stack and heights[i] >= heights[stack[-1]]:
                stack.pop()
                
            stack.append(i)
        return stack