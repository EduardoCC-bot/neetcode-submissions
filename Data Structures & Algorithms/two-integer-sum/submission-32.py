class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hasMap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hasMap:
                return [hasMap[diff], i]
            hasMap[nums[i]] = i 
        return []