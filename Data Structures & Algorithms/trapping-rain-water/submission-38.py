class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        prefix = [0] * n
        sufix = [0] * n 
        res = 0
        prefix[0] = height[0]
        for i in range(1,n):
            prefix[i] = max(height[i], prefix[i - 1])
        
        sufix[n-1] = height[n - 1]
        for i in range(n-2, -1, -1):
            sufix[i] = max(sufix[i+1], height[i])

        for i in range(n):
            res+= min(prefix[i], sufix[i]) - height[i]
        
        return res