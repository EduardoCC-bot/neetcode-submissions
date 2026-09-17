class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        frecMap = defaultdict(int)
        for n in hand:
            frecMap[n] += 1


        for i in sorted(frecMap.keys()):
            count = frecMap[i]
            if count > 0:
                for j in range(i, i + groupSize):
                    if frecMap[j] < count:
                        return False
                    frecMap[j] -= count
        return True

