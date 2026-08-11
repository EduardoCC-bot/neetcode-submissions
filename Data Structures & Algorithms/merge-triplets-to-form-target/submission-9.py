class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        res = [0,0,0]

        for triplet in triplets:
            if(triplet[0] > target[0] or triplet[1] > target[1] 
            or triplet[2] > target[2]):
                continue
            else:
                for i in range(3):
                    res[i] = max(triplet[i], res[i])

        return res == target

