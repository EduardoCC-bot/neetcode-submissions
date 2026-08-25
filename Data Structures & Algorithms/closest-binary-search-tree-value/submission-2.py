# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        res = root.val
        def dfs(node):
            nonlocal res
            if not node:
                return 
            
            res = min(node.val, res, key=lambda x: (abs(target-x), x))

            if node.val > target:
                dfs(node.left)
            else:
                dfs(node.right)
                
        dfs(root)
        return res
            