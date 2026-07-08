# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        lista_ant = dummy = ListNode()
        curr = head
        while curr:
            cola = curr
            prev = None
            expl = curr
            for _ in range(k):
                if not expl:
                    lista_ant.next = cola
                    return dummy.next #unir la lista y retornarla
                expl = expl.next

            for _ in range(k):
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            lista_ant.next = prev 
            lista_ant = cola
           
        return dummy.next 


        