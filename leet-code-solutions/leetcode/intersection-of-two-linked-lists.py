# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        dummya=ListNode(0,headA)
        dummyb=ListNode(0,headB)
        acur=dummya
        box=set()
        while acur:
            box.add(acur.next)
            acur=acur.next
        bcur=dummyb
        while bcur:
            if bcur.next in box:
                return bcur.next
            bcur=bcur.next