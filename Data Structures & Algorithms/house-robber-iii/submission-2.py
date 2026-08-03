# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node:
                return 0,0

            rob_left, skip_left = dfs(node.left)
            rob_right, skip_right = dfs(node.right)

            with_Root = node.val + skip_left + skip_right
            without_Root = max(skip_left, rob_left) + max(skip_right, rob_right)

            return with_Root, without_Root

        return max(dfs(root))