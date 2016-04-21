"""
	143. Reorder List

	Given a singly linked list L: L0->L1->...->Ln-1->Ln,
	reorder it to: L0->Ln->L1->Ln-1->L2->Ln-2->...

	You must do this in-place without altering the nodes' values.

	For example,
	Given {1,2,3,4}, reorder it to {1,4,2,3}.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderListII(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        

        stack = []
        curr = head
        while curr:
        	stack.append(curr)
        	curr = curr.next

        c = len(stack) / 2
        curr = head
        while stack and c > 0:
        	temp = stack.pop()
        	temp.next = curr.next
        	curr.next = temp
        	curr = curr.next.next
        	c -= 1
        curr.next = None
       	stack = []

    def reorderList(self, head):
    	"""
    		1.split into 2 lists
    		2.reverse the second list
    		3.merge the 2 lists
    	"""
    	if head and head.next.next:

    		l1 = head
    		l2 = head
    		while  l2.next and l2.next.next:
    			l1 = l1.next
    			l2 = l2.next.next

    		l2 = l1.next  # List 2
    		l1.next = None
    		l1 = head     # List 1
    	
    		# Now reverse List 2
    		dummyHead = ListNode('Dummy')
    		dummyHead.next = l2
    		while l2.next:
    			temp = l2.next
    			l2.next = temp.next
    			temp.next = dummyHead.next
    			dummyHead.next = temp

    		temp = None
    		l2 = dummyHead.next
    		
    	
    		# Merge l1 and l2

    		while l2:
    			dummyHead.next = l2.next
    			l2.next = l1.next
    			l1.next = l2
    			
    			l2 = dummyHead.next
    			l1 = l1.next.next

    		dummyHead = None
    		


def printL(head):
	res = []
	curr = head
	while curr:
		res.append(curr.val)
		curr = curr.next
	return res

L1 = ListNode(1)
L2 = ListNode(2)
L3 = ListNode(3)
L4 = ListNode(4)
L5 = ListNode(5)
L6 = ListNode(6)
L1.next = L2
L2.next = L3

L3.next = L4
L4.next = L5
L5.next = L6

print printL(L1)

sol = Solution()
sol.reorderList(L1)
print printL(L1)



