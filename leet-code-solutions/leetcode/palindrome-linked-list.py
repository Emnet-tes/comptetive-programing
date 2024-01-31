# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head 

         
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next 
        
        prev, curr = None, slow 

        
        while curr:
            nxt = curr.next 
            curr.next = prev 
            prev = curr
            curr = nxt 
        
        first, second= head, prev 

        
        while first and second:
            if first.val != second.val:
                return False 
            
            first = first.next 
            second = second.next 
        
        return True 