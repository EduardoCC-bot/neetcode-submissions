# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        '''
        1 -> 2 -> 3 -> 6 -> 4 -> 5 -> 6
        '''
        dummy = ListNode(next=head)
        prev = dummy
        curr = head
        while curr:
            nxt = curr.next
            if curr.val == val:
                prev.next = nxt
            else:
                prev = curr
            curr = curr.next
        return dummy.next
                