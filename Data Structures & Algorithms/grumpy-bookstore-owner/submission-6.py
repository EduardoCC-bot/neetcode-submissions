class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        l = 0 
        n = len(customers) 
        happy, act = 0, 0
        for i in range(n):
            if grumpy[i] == 0:
                happy += customers[i]
            if i < minutes and grumpy[i] == 1:
                act += customers[i]
        res = act
        for r in range(minutes,n):
            if grumpy[r] == 1:
                act += customers[r]
            if grumpy[l] == 1:
                act -= customers[l]
            l+=1
            res = max(act, res)
        return res + happy

        