"""
	82. Remove Duplicates from Sorted List II

	https://leetcode.com/problems/remove-duplicates-from-sorted-list-ii/

	Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.

	For example,
		Given 1->2->3->3->4->4->5, return 1->2->5.
		Given 1->1->1->2->3, return 2->3.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        th = ListNode(None)
        th.next = head
        """
        th2 = ListNode(None)
        th2.next = th
        """
       
        h1 = th

        while h1 and h1.next :
        	val = h1.next.val
        	h2 = h1.next.next
        	count = 0
        	while h2 and h2.val == val:
        		h2 = h2.next
        		count = 1
        	if count == 0:
        		h1 = h1.next
        	else:
        		h1.next = h2

        return th.next

    def deleteDuplicatesII(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        th = ListNode(None)
        th.next = head
    
        h1 = th

  
        while h1 and h1.next :
        
        	val = h1.next.val
        	h2 = h1.next.next
        	temp = h1.next
        	count = 0

        	while True:
        		while h2 and h2.val == val:
        			h2 = h2.next
        			count = 1
        		if count == 0:        			
        			break
        		else:
        			temp = h2
        			if h2:
        				val = h2.val
        				h2 = h2.next
        				count = 0
        			else:
        				
        				break
        	h1.next = temp
        	h1 = h1.next
        return th.next

    def deleteDuplicatesIII(self, head):

    	dummy = ListNode('None')
    	pt = dummy
    	repeated = 0

    	while head and head.next:
    		if head.val != head.next.val:
    			if not repeated:
    				pt.next = head
    				pt = pt.next
    			repeated = 0
    		else:
    			repeated = 1
    		head = head.next

    	pt.next = None if repeated else head

    	return dummy.next


sol = Solution()
n1 = ListNode(1)
n11 = ListNode(1)
n2 = ListNode(2)
n22 = ListNode(2)
n3 = ListNode(3)
n33 = ListNode(3)
n4 = ListNode(4)
n44 = ListNode(4)
n5 = ListNode(5)
n55 = ListNode(5)

n1.next = n11

n11.next = n2

n2.next = n22

n22.next = n3
n3.next = n4
n4.next = n44
n44.next = n5
n5.next = n55


nt = n1


while nt:
	print nt.val
	nt = nt.next
print 


res = sol.deleteDuplicatesIII(n1)

while res:
	print res.val
	res = res.next
