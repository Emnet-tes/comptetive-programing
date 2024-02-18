# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        current=head
        size=0
        while current:
            size+=1
            current=current.next
        diff=size-n
        dummy=ListNode(0,head)
        current=dummy.next
        prev=dummy
        i=0
        while current and i<diff :
            prev=current
            current=current.next
            i+=1
        
        prev.next=current.next

        return dummy.next