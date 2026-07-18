class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        The firts thing that comes to my mind is to have a window starting 
        cnt
        [1,0,1,1,0]
        check the element 0
            is 1
                calculate the size of window = 1
        check element 1:
            is 0
                we have a flip
                    yes
                        calculate the size of window 2
        checl element 2:
            is 1
                calculate size 3

        check element 3:
            is 1
                calculate size 3
        
        check  element 4
            is 0
                we have a flip
                    no
                        move l pointer
                            is l 0 : flip true
                                no
                            

        """
        
        l = 0
        maxsize = 0
        num0 = 0
        for r in range(len(nums)): 
            if nums[r] == 0:
                num0 += 1

            while num0 == 2:
                if nums[l] == 0:
                    num0-=1
                l+=1
            maxsize = max(maxsize, r-l+1)
            r+=1

        return maxsize