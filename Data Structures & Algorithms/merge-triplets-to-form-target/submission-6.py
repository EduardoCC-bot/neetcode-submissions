class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        valid = 0
        res = []
        if len(triplets) == 1 and triplets[0] == target: return True

        for triplet in triplets:
            if(triplet[0] > target[0] or triplet[1] > target[1] 
            or triplet[2] > target[2]):
                continue
            else:
                if not res: res = triplet.copy()
                for i in range(3):
                    res[i] = max(triplet[i], res[i])

        return res == target

