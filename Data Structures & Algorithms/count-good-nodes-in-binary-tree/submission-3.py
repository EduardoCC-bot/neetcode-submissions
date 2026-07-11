# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''  
        stack -> 2
        maximun : 2
        
        stack -> 1 left, 1 right
        x.value < maximun value --> Is not a good node
         2 < 1 --> NOT GOOD ONE
        
        maximun : 2
        stack -> 3 left, 1 right level up '1'
        2 < 3 ---> GOOD ONE
        maximun: 3

        stack -> 1 
        3 < 1--> NOT GOOD ONE

        stack 1 left, 5 right
        1 < 3 --> NOT GOOD ONE

        stack 5 right
        3 < 5 --> GOOD ONE

        '''
        stack = [(root, root.val)] # 2
        goodNodes = 0
        while stack: # 1 element | 2 elements | 3 elements
            node, last_max = stack.pop() # 2 | 1 right | 5
            if last_max <= node.val: # 2 <= 2 | 2 <= 1 
                goodNodes += 1  # goodNodes = 1 | goodNodes = 1 | goodNodes = 2
            
            last_max = max(last_max, node.val) # 2, 2: 2| 2, 1: 2 | 2, 5: 5

            if node.right: # 1
                stack.append((node.right, last_max)) # [1,1] | [1 main_left, 1 right_left, 5]
             # [1 main_left, 1 right_left]
            if node.left:   # 1 | 1 | NONE
                stack.append((node.left, last_max)) # [1] | [1 main_left, 1 right_left] 

        return goodNodes
            



