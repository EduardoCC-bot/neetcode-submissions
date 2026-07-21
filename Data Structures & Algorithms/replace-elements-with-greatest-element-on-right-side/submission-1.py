class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        """
        Optimize go through the array from right to left
        arr = [2,4,5,3,1,2]
        """
        n = len(arr)
        res = [0] * n
        maxNum = -1
        for i in range(n - 1, -1, -1):
            res[i] = maxNum
            maxNum = max(arr[i], maxNum)
        return res