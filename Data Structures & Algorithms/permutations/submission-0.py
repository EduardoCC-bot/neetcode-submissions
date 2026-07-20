class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = [False for i in range(len(nums))] # [F,F,F] 
        def helper(i, curr, n): # 0, [], [F,F,F] | 1, [1] [T,F,F]
            if len(curr) == len(nums): # 0 == 3 | 1 == 3
                res.append(curr.copy())
                return
            
            for j in range(len(n)): #0 |0 | 1
                if not n[j]: #[F] | [T] [F]
                    curr.append(nums[j]) # [1] | [1,2]
                    n[j] = True #[T,F,F] | [T,T,F]
                    helper(j, curr,n) # 0, [1], [T,F,F] | 
                    curr.pop()
                    n[j] = False

            
        helper(0,[], n)
        return res
            
            
            
            
        