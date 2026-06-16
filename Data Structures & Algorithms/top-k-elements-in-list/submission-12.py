class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = defaultdict(int)
        res = []
        for n in nums:
            hashMap[n] += 1
            print(hashMap.get(n))
        elementos_repetidos = sorted(hashMap.items(), key=lambda item : item[1], reverse = True)
        
        for i in range(k):
            res.append(elementos_repetidos[i][0])
        return res

