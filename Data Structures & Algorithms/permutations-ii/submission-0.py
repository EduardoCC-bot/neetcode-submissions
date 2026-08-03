class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        """
        nums = [1,1,2]
        """
        res = []
        curr = []
        n = {n:0 for n in nums }
        for nu in nums:
            n[nu] += 1

        def helper():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for num in n:
                if n[num] > 0:
                    curr.append(num)
                    n[num] -= 1
                    helper()
                    n[num] += 1
                    curr.pop()

        helper()
        return res