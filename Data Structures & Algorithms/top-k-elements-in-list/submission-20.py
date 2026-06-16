class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        buckets = [[] for i in range(len(nums)+ 1)]
        res = []

        for n in nums:
            hashMap[n] += 1
        
        for num, cnt in hashMap.items():
            buckets[cnt].append(num)
        
        for i in range(len(buckets)-1, 0, -1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k:
                    return res

