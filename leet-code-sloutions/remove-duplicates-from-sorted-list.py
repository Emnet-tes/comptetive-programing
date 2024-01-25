# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        current=None
        prev=None
        if head:
            current=head.next
            prev=head

        while current:
            if prev.val==current.val:
                if not current.next:
                    prev.next=None
                    return head
                current=current.next
                
            else:
                prev.next=current
                prev=current
                current=current.next
        
        return head
        