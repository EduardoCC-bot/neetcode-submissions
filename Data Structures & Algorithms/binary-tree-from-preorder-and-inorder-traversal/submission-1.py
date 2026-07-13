# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        """
        perorder = [1, 2, 3, 4]
        
        inorder = [2, 1, 3, 4]
        

        root firts element  on preorder
        pointer on inorder i 
        validate if pointer is equal to the root, if it is que have to estar adding on the right
        while not we have to add on the left

        root = 1
        i = 0
        while inorder[i] != root.value:
           add to the left

        while i < len(inorder)
            add to the right
        """
        if not preorder or not inorder: return None
        root = TreeNode(preorder[0])

        m = inorder.index(preorder[0]) 

        root.left = self.buildTree(preorder[1:m+1], inorder[:m])
        root.right = self.buildTree(preorder[m+1:], inorder[m+1:])
        
        return root

        


