class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        hand = [1,2,3,3,4,5,6,7]
        frecMap = {1:1, 2:1, 3:2, 4:1, 6:1, 7:1}
        sort hand
        loop
            is i in frecMap: 
               frecMap[i]-= 1
        """
        if len(hand) % groupSize != 0:
            return False
        frecMap = defaultdict(int)
        
        for n in hand:
            frecMap[n] += 1
        hand.sort()
        for i in range(len(hand)):
            if frecMap[hand[i]] > 0:
                for j in range(hand[i], hand[i] + groupSize):
                    if frecMap[j] <= 0:
                        return False
                    else:
                        frecMap[j] -= 1
        return True

