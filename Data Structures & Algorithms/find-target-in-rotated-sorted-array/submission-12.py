class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        target = 1, 4
        [3,4,5,6,1,2] len = 6
        [3,5,6,0,1,2]

        l = 0
        r = 5
        mid = 2
        l = 3
        r = 5
        mid = 4

        """
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + ((r - l) // 2)
            if nums[mid] == target:
                return mid
            if nums[mid] <= nums[r]:
                #Right is the sorted Part 
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
            else:
                #Left is the sorted Part 
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1 

        return -1
                