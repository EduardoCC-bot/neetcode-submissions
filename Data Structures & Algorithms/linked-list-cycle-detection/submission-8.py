# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        bunny = head
        turtle = head

        while(bunny and bunny.next):
            bunny = bunny.next.next
            turtle = turtle.next
            
            if (bunny == turtle):
                return True
            
        return False
        
