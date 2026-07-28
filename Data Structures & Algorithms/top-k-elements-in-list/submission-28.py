class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        buckets = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] += 1
        
        for n, cnt in count.items():
            buckets[cnt].append(n)
        
        res = []
        for i in range(len(buckets) - 1, 0, -1):
            for n in buckets[i]:
                res.append(n)
                if len(res) == k:
                    return res
                
        
