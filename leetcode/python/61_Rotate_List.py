"""
	61. Rotate List

	Given a list, rotate the list to the right by k places, where k is non-negative.

	For example:
	Given 1->2->3->4->5->NULL and k = 2,
	return 4->5->1->2->3->NULL.


        
"""

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
        	return [0]

        tempHead = ListNode(0)
        tempHead.next = head

        l1 = head
        
        t = 1
        while t <= k and l1.next != None:
        	l1 = l1.next
        	t += 1
        
        
        newK = k % t

        if newK != 0:
        	t = 1
        	l1 = head
        	while t <= newK:
        		l1 = l1.next
        		t += 1
        	
        	l2 = head
        	while l1.next != None:
        		l1 = l1.next
        		l2 = l2.next
        
        	tempHead.next = l2.next	
        	l2.next = None
        	l1.next = head

        return tempHead.next


    def rotateRight2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head == None:
        	return [0]

        tempHead = ListNode(0)
        tempHead.next = head

        l1 = head
        l2 = head
        t = 0
        while t < k:
        	if l1.next != None:
        		l1 = l1.next
        		t += 1
        	else:
        		l1 = head
        		t += 1
     
        while l1.next != None:
        	l1 = l1.next
        	l2 = l2.next
        
        if l2.next != None:
        	tempHead.next = l2.next	
        	l2.next = None
        	l1.next = head

        return tempHead.next


def printList(head):
	res = []
	t = head
	while t:
		res.append(t.val)
		t = t.next
	return res

sol = Solution()
n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(6)
n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6

pn1 = printList(n1)
print pn1

import time
s1 = time.time()
for i in range(100):
	rn1 = sol.rotateRight(n1,6666)
e1 = time.time()
#prn1 = printList(rn1)
#print prn1

s2 = time.time()
for i in range(100):
	rn1 = sol.rotateRight2(n1,6666)
e2 = time.time()

print e1 - s1
print e2 - s2

