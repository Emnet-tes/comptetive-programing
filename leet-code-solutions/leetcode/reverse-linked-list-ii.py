# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        box = []
        while head is not None:
            box.append(head.val)
            head = head.next
        left -=1
        right -=1
        while left<right:
            box[left],box[right] = box[right],box[left]
            left +=1
            right -=1
        h = None
        t = None
        for i in box:
            node = ListNode(i)
            if h is None:
                h = node
                t = node
            else:
                t.next = node
                t = node
        return h