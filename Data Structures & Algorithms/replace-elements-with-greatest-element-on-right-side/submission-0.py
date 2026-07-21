class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        BRUTE FORCE
        arr = [2,4,5,3,1,2]
        """
        maxNum = 0
        for i in range(len(arr)): # [2] # [4]
            for j in range(i+1, len(arr)): # [4] # [5]
                maxNum = max(maxNum, arr[j]) # 4, 5, 5
            arr[i] = maxNum # [5,4,5,3,1,2]
            maxNum = 0 # 0
        arr[-1] = -1
        
        return arr