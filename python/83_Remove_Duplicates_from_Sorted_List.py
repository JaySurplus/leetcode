"""
	83. Remove Duplicates from Sorted List

	Given a sorted linked list, delete all duplicates such that each element appear only once.

	For example,
	Given 1->1->2, return 1->2.
	Given 1->1->2->3->3, return 1->2->3.

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
       # th = ListNode('None')
        th = head 

        while th :
        	while th.next and th.val == th.next.val:
        		th.next = th.next.next
        	
        	th = th.next
        return head	







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
n11.next = ListNode(1)
"""
n2.next = n22

n22.next = n3
n3.next = n4
n4.next = n44
n44.next = n5
n5.next = n55
"""

nt = n1


while nt:
	print nt.val
	nt = nt.next
print 


res = sol.deleteDuplicates(n1)

while res:
	print res.val
	res = res.next
