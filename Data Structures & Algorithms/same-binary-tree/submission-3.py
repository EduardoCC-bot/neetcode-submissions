# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        qp = deque([p])
        qq = deque([q])
        
        while qp and qq:
            for _ in range(len(qp)):
                nodep = qp.popleft()
                nodeq = qq.popleft()

                if nodep is None and nodeq is None:
                    continue
                if nodep is None or nodeq is None or nodep.val != nodeq.val:
                    return False
                
                qp.append(nodep.left)
                qp.append(nodep.right)
                qq.append(nodeq.left)
                qq.append(nodeq.right)
        
        return True

