class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        next_red, next_blue, current = 0, len(nums) - 1, 0

        while current <= next_blue:
            if nums[current] == 0:
                aux = nums[next_red]
                nums[next_red] = nums[current]
                nums[current] = aux
                next_red += 1
                current += 1
            elif nums[current] == 2:
                aux = nums[next_blue]
                nums[next_blue] = nums[current]
                nums[current] = aux
                next_blue -= 1
            else:
                current+=1
                
 

        