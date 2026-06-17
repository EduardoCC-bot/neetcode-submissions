class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashSet = set(nums)
        longest = 0

        for n in hashSet:
            if (n - 1) not in hashSet:
                lenght = 1
                while(n + lenght) in hashSet:
                    lenght += 1
                longest = max(lenght, longest)

        return longest