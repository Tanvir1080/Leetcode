# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        number1 = []
        number2 = []
        
        head = current = ListNode(0)
        firstNode = True
        while l1:
            number1.insert(0, l1.val)
            l1 = l1.next
        while l2:
            number2.insert(0, l2.val)
            l2 = l2.next
        print(number1, number2)
        
        number1 = int(''.join(str(digit) for digit in number1))
        number2 = int(''.join(str(digit) for digit in number2))
        number3 = str(number1 + number2)
        
        for letter in reversed(number3):
            current.next = ListNode(letter) 
            current = current.next
            
        return head.next
    
    