"""
	86. Partition List

	Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.

	You should preserve the original relative order of the nodes in each of the two partitions.

	For example,
	Given 1->4->3->2->5->2 and x = 3,
	return 1->2->2->4->3->5.

	https://leetcode.com/problems/partition-list/
"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
        	return

        tempHead = ListNode(None)
        tempHead.next = head

       
        h1 = tempHead
       	h2 = tempHead

        while h1.next:
        	if h1.next.val < x:
        		if h1 == h2:
        			h1 = h1.next
        			h2 = h2.next
        		else:
        			temp = h1.next
        			h1.next = temp.next
        			temp.next = h2.next
        			h2.next = temp
        			h2 = h2.next
        	else:
        		h1 = h1.next
        return tempHead.next
    def partitionII(self, head, x):

    	newHead = ListNode('newHead')

    	tempHead = ListNode('tempHead')
    	tempHead.next = head

    	h1 = tempHead
    	h2 = newHead
    	while h1.next:
    		if h1.next.val < x:
    			temp = h1.next
    			h1.next = temp.next
    			temp.next = None
    			h2.next = temp
    			h2 = h2.next
    		else:
    			h1 = h1.next
    	h2.next = tempHead.next
    	tempHead.next = None
    	return newHead.next



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

n1.next = n4
n4.next = n3
n3.next = n2
n2.next = n5
n5.next = n22

nt = n1

while nt:
	print nt.val
	nt = nt.next
print 

 
res = sol.partitionII( n1 , 3)

while res:
	print res.val
	res = res.next