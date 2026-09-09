class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numsMap = defaultdict(int)
        nums.sort()
        res = []
        for n in nums:
            numsMap[n] += 1

        for i in range(len(nums)):
            numsMap[nums[i]] -= 1
            if(i and nums[i] == nums[i-1]):
                continue


            for j in range(i+1, len(nums)):
                numsMap[nums[j]] -= 1
                if(j - 1 > i and nums[j] == nums[j-1]):
                    continue
                target = -(nums[i] + nums[j])
                if(numsMap[target] > 0):
                    res.append( [nums[i], nums[j], target] )
                
            for j in range( i + 1, len(nums)):
                numsMap[nums[j]] += 1
            
        return res


