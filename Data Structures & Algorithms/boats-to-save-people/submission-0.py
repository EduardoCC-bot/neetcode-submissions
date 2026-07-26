class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        """
        [5,4,1,2]
        [1,2,4,5]
         l l r r
        [1,5]
        [2,4]
        [1,3,2,3,2]
        [1,2,2,3,3]
         l       r
           r r r
           l
         [3]
         [3]
         [1,2]
         [2]

        limit of 3        
        O(log(n))
        O(nlongn)
        """
        people.sort()
        l, r = 0, len(people) - 1
        cnt = 0 
        while l <= r:
            sumweight = people[l] + people[r]
            if sumweight <= limit:
                l+=1
                r-=1                
            else:
                r-=1
            cnt+=1
        return cnt
