# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        
        slow = head
        fast = head

        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
        
        reverse = None

        while slow !=None:
            next = slow.next
            slow.next = reverse
            reverse = slow
            slow = next

        slow = head

        while reverse != None:
            #print(f"{reverse.val}  {slow.val}")

            if slow.val != reverse.val:
                return False
            
            slow = slow.next
            reverse = reverse.next
        

        return True