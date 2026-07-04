# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        frente = atras = dummy
        for i in range (n): 
            frente = frente.next
        
        while frente.next:
            atras = atras.next
            frente = frente.next
        
        atras.next = atras.next.next
        
        return dummy.next
        

        
