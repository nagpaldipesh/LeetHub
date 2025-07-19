# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        
        p1 = headA
        p2 = headB

        while(p1 != p2):
            p1 = p1.next if p1 else headB
            p2 = p2.next if p2 else headA
            # if p1 == None:
            #     p1 = headB
            # else:
            #     p1 = p1.next

            # if p2 == None:
            #     p2 = headA
            # else:
            #     p2 = p2.next
        
        return p1