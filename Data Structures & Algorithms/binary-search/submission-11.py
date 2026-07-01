class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            half = l + (r - l) // 2
            if nums[half] < target:
                l = half + 1
            elif nums[half] > target:
                r = half - 1
            else:
                return half
        return -1