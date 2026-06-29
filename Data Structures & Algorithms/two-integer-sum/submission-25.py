class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        diff = 0
        for i in range(len(nums)):
            hashMap[nums[i]] = i

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap and i != hashMap[diff]:
                return [i, hashMap[diff]] 
        