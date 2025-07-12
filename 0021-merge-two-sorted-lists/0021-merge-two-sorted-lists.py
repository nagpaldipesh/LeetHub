# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        pointer = dummy

        while list1 != None and list2 != None:
            if list1.val <= list2.val:
               pointer.next = ListNode(list1.val)
               list1 = list1.next
            else:
                pointer.next = ListNode(list2.val)
                list2 = list2.next
            
            pointer = pointer.next 

        if list1 != None:
            pointer.next = list1
        elif list2 != None:
            pointer.next = list2

        return dummy.next
        