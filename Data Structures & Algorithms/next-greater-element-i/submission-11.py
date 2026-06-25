class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapa = {}
        for i in range(len(nums2)):
            while stack and nums2[i] > stack[-1]:
                mapa[stack.pop()] = nums2[i]
            stack.append(nums2[i])
        res = [-1] * len(nums1)
        for j in range(len(nums1)):
            if nums1[j] in mapa:
                res[j] = mapa[nums1[j]]
        return res
