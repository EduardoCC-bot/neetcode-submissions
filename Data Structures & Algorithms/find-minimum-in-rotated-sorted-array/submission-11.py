class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        [3,4,5,6,1,2]

        [9,-5,-2,0,3]

        """
        l, r = 0 , len(nums) - 1

        while l <= r:
            m = l + (r - l)//2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[l] < nums[m]:
                r = m - 1
            else:
                l+=1
                r-=1
        return nums[m]

