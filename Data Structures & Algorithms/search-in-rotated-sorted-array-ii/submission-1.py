class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        '''
        target = 1
        [3,4,4,5,6,1,2,2]
         l     m       r           
               l   m   r

        Binary search
        two pointers
        if l < r -> Correct parte array
        if l > r -> Rotated part array

        '''
        l, r = 0, len(nums) - 1

        while l <= r:
            m = l + (r-l) // 2
            if nums[m] == target: return True

            if nums[l] < nums[m]:
                if nums[l] <= target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
            elif nums[l] > nums[m]:
                if nums[m] < target <= nums[r]:
                    r = m + 1
                else:
                    r = m - 1
            else:
                l += 1
        
        return False