class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writer,current = 2, 2

        while current < len(nums):
            if nums[current] != nums[writer - 2]:
                nums[writer] = nums[current]
                writer += 1
            current+=1
        return writer