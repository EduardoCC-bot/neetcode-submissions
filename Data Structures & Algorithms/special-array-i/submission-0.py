class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        '''
        nums = [4,  3,    1, 6]
                i  i+1
        O(n)

        Validate
            1 i is even
                1.1 i+1 is odd

            2 i is odd
                2.1 i+1 is even
        '''

        for i in range(1, len(nums)):
            if nums[i - 1] % 2 == nums[i] % 2:
                return False
        return True