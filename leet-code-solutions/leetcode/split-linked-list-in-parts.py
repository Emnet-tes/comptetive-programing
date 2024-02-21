# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        size=0
        dummy=ListNode(0,head)
        current=dummy.next
        while current:
            size+=1
            current=current.next
        first_size=size%k
        ans=[]
        current=dummy.next

        for i in range(k):
            ans.append(current)
            n=size//k
            if first_size:
                n+=1
                first_size-=1
            for j in range(n-1):
                current=current.next
            if current:
                current.next,current=None,current.next
        return ans


        return ans
