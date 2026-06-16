class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        res = []
        for n in nums:
            if n in hashMap:
                hashMap[n] = hashMap[n] + 1
            else:
                hashMap[n] = 1
        
        elementos_repetidos = sorted(hashMap.items(), key=lambda item : item[1], reverse = True)
        for i in range(k):
            res.append(elementos_repetidos[i][0])

        return res