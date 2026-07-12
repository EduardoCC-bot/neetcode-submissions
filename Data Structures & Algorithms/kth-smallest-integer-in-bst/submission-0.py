# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        Kth smallest value of the right
        DFS
        array store [2, 1, 3]

        stack = [4]

        node = 4 
        sortedArray [4]
        stack [5, 3]
        
        node : 3
        sortedArray [4, 3]
        stack [5, 2]
        sortedArray [4,3,2]
        stack [5, 1]
        node 1
        sortedArray[4,3,2,1]
        stack [5]
        node 5
        sortedArray [4,3,2,1,5]
        kth: 4
        '''

        stack = [root]      # node  2
        Sorted_array = []  # []

        while stack:  # 1 elemnt | 2 elements
            node = stack.pop() # node: 2 | node :1 | node : 3
            Sorted_array.append(node.val) # [2], [2,1,3]

            if node.right: # 3 | None
                stack.append(node.right) # [3] | [3] 
            if node.left: # 1
                stack.append(node.left) # [3,1] | [3]
        Sorted_array.sort()
        return Sorted_array[k-1] # [4,3,2,5] k = 4-1: 3
            



