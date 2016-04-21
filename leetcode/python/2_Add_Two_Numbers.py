# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        dummy = ListNode('temp')
        curr = dummy
        
        
        while l1 and l2:
            a = l1.val
            b = l2.val
            s = a + b + carry
            carry = s/10
            curr.next = ListNode(s%10)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
            
        if l1:
            l = l1
        else:
            l = l2
        
         
        
        while l:
            a = l.val
            s = a + carry
            carry = s/10
            curr.next = ListNode(s%10)
            curr = curr.next
            l = l.next
        if carry:
            curr.next = ListNode(carry)
        
        return dummy.next
            
        