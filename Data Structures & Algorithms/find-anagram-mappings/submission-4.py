class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mapa = {}
        for i in range(len(nums2)):
            mapa[nums2[i]] = i
        
        res = [] #[0] * len(nums1)
        for i in range(len(nums1)):
            res.append(mapa[nums1[i]])
        return res

        