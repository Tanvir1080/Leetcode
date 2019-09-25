# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 and not l2: 
            return None
        if not l1 and l2: 
            return l2
        if not l2 and l1: 
            return l1
        
        head = current = ListNode(0)
        
        while l1 and l2: 
            
            if l1.val < l2.val: 
                current.next = ListNode(l1.val)
                l1 = l1.next
            else:
                current.next = ListNode(l2.val)
                l2 = l2.next
            
            current = current.next
        
        if not l1: 
             current.next = l2
        else: 
            current.next = l1
            
        return head.next