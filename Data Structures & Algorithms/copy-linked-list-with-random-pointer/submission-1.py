"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        mapa = defaultdict(lambda: Node(0))
        
        ptr = head
        mapa[None] = None
        while ptr:
            mapa[ptr].val = ptr.val
            mapa[ptr].next = mapa[ptr.next]
            mapa[ptr].random = mapa[ptr.random]
            ptr = ptr.next
        
        return mapa[head]



