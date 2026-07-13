class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        curr = m
        for i in range(len(nums2)):
            nums1[curr] = nums2[i]
            curr +=1
        
        nums1.sort()
        return nums1
        
        
        