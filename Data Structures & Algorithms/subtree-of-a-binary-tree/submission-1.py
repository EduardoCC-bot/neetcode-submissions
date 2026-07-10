# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        while stack:
            node = stack.pop()
            #2 casos 
            # Es igual a nodo que estamos viendo en subroot
            if node.val == subRoot.val:
                if self.sameTree(node, subRoot): 
                    return True
            # No es igual al nodo que estamos viendo en subroot
            if node.left: stack.append(node.left)
            if node.right: stack.append(node.right)

        return False

    def sameTree(self, tree1, tree2):
        stack = [(tree1, tree2)]

        while stack:
            node1, node2 = stack.pop()            
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((node1.right, node2.right))
            stack.append((node1.left, node2.left))
            
        return True
            
