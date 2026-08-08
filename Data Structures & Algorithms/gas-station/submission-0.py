class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost): return -1
        n = len(gas)
        res = 0
        diff = 0
        for i in range(n):
            diff += gas[i] - cost[i]
            if diff < 0: 
                diff = 0
                res = i + 1
        return res

            