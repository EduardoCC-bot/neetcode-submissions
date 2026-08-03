class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res =  []
        curr = []
        hashMap = {n:0 for n in nums}
        for n in nums:
            hashMap[n] += 1
        
        def helper():
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            
            for n in hashMap:
                if hashMap[n] > 0:
                    curr.append(n)
                    hashMap[n] -= 1
                    helper()
                    hashMap[n] += 1
                    curr.pop()     
        helper()
        return res
